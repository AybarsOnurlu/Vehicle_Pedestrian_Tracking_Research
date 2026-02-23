# Architecture Design Document
## Real-Time Vehicle & Pedestrian Detection and Tracking System

---

## 1. System Overview

This document describes the architectural design of a real-time vehicle and pedestrian detection and tracking system built on the **Tracking-by-Detection (TBD)** paradigm. The system ingests video streams, detects objects using deep neural networks, associates detections across frames to maintain persistent identities, and outputs annotated results.

---

## 2. Architectural Pattern: Pipe-and-Filter

The system follows a **Pipe-and-Filter** architecture where data flows synchronously through isolated processing nodes. Each node (filter) performs a single responsibility, receives input from the previous stage, and passes output to the next.

### Benefits:
- **Modularity**: Swap detectors (YOLOv8 → YOLOv9) or trackers (ByteTrack → DeepSORT) without affecting other stages
- **Testability**: Each node can be unit-tested in isolation
- **Scalability**: Individual nodes can be optimized independently (e.g., TensorRT only on inference node)

---

## 3. Pipeline Stages

### 3.1 Ingestion Node
| Property | Detail |
|----------|--------|
| **Input** | MP4 file path, RTSP URL, or camera device ID |
| **Output** | Raw BGR frames (NumPy arrays) in thread-safe queue |
| **Key Tech** | OpenCV `VideoCapture`, FFmpeg backend |
| **Responsibilities** | Frame decoding, FPS regulation, reconnection handling |

### 3.2 Preprocessing Node
| Property | Detail |
|----------|--------|
| **Input** | Raw BGR frames |
| **Output** | Normalized GPU tensors (batch × 3 × H × W) |
| **Key Tech** | OpenCV resize, NumPy, PyTorch tensor ops |
| **Responsibilities** | Letterbox resize, pixel normalization (0–1), BGR→RGB, HWC→CHW transpose |

### 3.3 Inference Node (YOLOv8 Detector)
| Property | Detail |
|----------|--------|
| **Input** | Preprocessed GPU tensors |
| **Output** | Raw bounding boxes + confidence scores + class logits |
| **Key Tech** | Ultralytics YOLOv8 |
| **Responsibilities** | Forward pass execution, multi-scale feature extraction |

### 3.4 Post-Processing Node
| Property | Detail |
|----------|--------|
| **Input** | Raw detector output |
| **Output** | Filtered detections `[x1, y1, x2, y2, conf, class_id]` |
| **Key Tech** | torchvision NMS, confidence thresholding |
| **Responsibilities** | Non-Maximum Suppression, confidence filtering, coordinate scaling |

### 3.5 Tracking Node
| Property | Detail |
|----------|--------|
| **Input** | Filtered detections per frame |
| **Output** | Tracked objects with persistent IDs `[x1, y1, x2, y2, track_id, class_id]` |
| **Key Tech** | Kalman Filter (FilterPy), Hungarian (SciPy), ByteTrack/DeepSORT |
| **Responsibilities** | State prediction, data association, track lifecycle management |

**Key Sub-Components:**
```
Tracking Node
├── Kalman Filter (Motion Model)
│   ├── Predict: Project state to next frame
│   └── Update: Incorporate matched detection
├── Cost Matrix Builder
│   ├── IoU Distance (spatial)
│   └── Cosine Distance (appearance, DeepSORT only)
├── Hungarian Algorithm (Assignment)
│   ├── First Pass: High-confidence matching
│   └── Second Pass: Low-confidence recovery (ByteTrack)
└── Track Manager
    ├── Active Tracks Registry
    ├── Lost Tracks Buffer (track_buffer frames)
    └── Track Deletion Logic
```

### 3.6 Output Node
| Property | Detail |
|----------|--------|
| **Input** | Tracked objects + original frame |
| **Output** | Annotated video frame + JSON metadata record |
| **Key Tech** | OpenCV drawing, JSON serialization |
| **Responsibilities** | BBox rendering, ID labels, trajectory tails, metadata export |

---

## 4. Data Flow Diagram

```
                    ┌─────────────────────────────────────────────────────────┐
                    │                    PIPELINE RUNNER                       │
                    │                                                         │
  Video Source ────▶│  Ingest ──▶ Preprocess ──▶ Detect ──▶ Track ──▶ Output │────▶ Annotated Video
                    │                                                         │────▶ JSON Metadata
                    │            configs/          models/       configs/      │────▶ System Logs
                    └─────────────────────────────────────────────────────────┘
```

---

## 5. Model Architecture

### YOLOv8 Detection Head
```
Input Image (1280×1280)
       │
       ▼
┌──────────────┐
│   Backbone   │  CSPDarknet53 (Feature Extraction)
│   (C2f + SPPF)│
└──────┬───────┘
       │
       ▼
┌──────────────┐
│     Neck     │  PANet + FPN (Multi-Scale Feature Fusion)
│   (P3/P4/P5) │
└──────┬───────┘
       │
       ▼
┌──────────────────────────┐
│   Decoupled Head         │
│  ┌──────────┬──────────┐ │
│  │  Cls Head│  Reg Head│ │  Separate classification & regression
│  └──────────┴──────────┘ │
└──────────────────────────┘
       │
       ▼
  Anchor-Free Predictions
  (class_probs, bbox_coords)
```

### Model Scale Comparison
| Variant | Parameters | mAP@0.5 (COCO) | FPS (T4 GPU) | Recommended Use |
|---------|-----------|-----------------|---------------|-----------------|
| YOLOv8n | 3.2M | 37.3 | 170 | Ultra-low latency edge |
| YOLOv8s | 11.2M | 44.9 | 120 | Edge deployment |
| **YOLOv8m** | **25.9M** | **50.2** | **80** | **Prototype baseline** |
| YOLOv8l | 43.7M | 52.9 | 50 | High-accuracy research |
| YOLOv8x | 68.2M | 53.9 | 35 | Maximum accuracy |

---

## 6. Tracking Algorithm Selection

| Algorithm | Speed | Occlusion Handling | Re-ID | Best For |
|-----------|-------|-------------------|-------|----------|
| **SORT** | ★★★★★ | ★★☆☆☆ | ❌ | Low-latency, sparse scenes |
| **DeepSORT** | ★★★☆☆ | ★★★★☆ | ✅ | Identity-critical applications |
| **ByteTrack** | ★★★★★ | ★★★★★ | ❌ | Dense traffic, frequent occlusions |

**Primary Choice: ByteTrack** — Preserves trajectories through heavy occlusions without Re-ID overhead.

---

## 7. Evaluation Framework

```
Evaluation Suite
├── Detection Metrics
│   ├── mAP@0.5          (Standard COCO threshold)
│   └── mAP@0.5:0.95     (Strict localization quality)
├── Tracking Metrics
│   ├── MOTA             (Aggregated error rate)
│   ├── MOTP             (Localization precision)
│   ├── IDF1             (Identity preservation quality)
│   └── HOTA             (Balanced detection + association)
└── Performance Metrics
    ├── GPU Latency (ms)  (Per-frame inference time)
    └── End-to-End FPS    (Full pipeline throughput)
```

---

## 8. Key Design Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Detection architecture | YOLOv8 (anchor-free) | Best speed/accuracy trade-off; no anchor-box overhead |
| Primary tracker | ByteTrack | Occlusion robustness without Re-ID computational cost |
| Motion model | Linear Kalman Filter | Sufficient for road-scene constant-velocity assumption |
| Annotation format | YOLO TXT (normalized) | Native compatibility with Ultralytics training pipeline |
| Config management | YAML files | Human-readable; Git-trackable; no code changes needed |
| CLI interface | argparse | Standard Python; no external dependencies |
