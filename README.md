<div align="center">

# 🚗 Real-Time Vehicle & Pedestrian Detection and Tracking

**A production-grade multi-object tracking system built on the Tracking-by-Detection paradigm**

[![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-3776AB?logo=python&logoColor=white)](https://python.org)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0%2B-EE4C2C?logo=pytorch&logoColor=white)](https://pytorch.org)
[![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-00FFFF?logo=yolo&logoColor=white)](https://docs.ultralytics.com)
[![TensorRT](https://img.shields.io/badge/TensorRT-FP16%2FINT8-76B900?logo=nvidia&logoColor=white)](https://developer.nvidia.com/tensorrt)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?logo=docker&logoColor=white)](https://docker.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

[Architecture](#-architecture) · [Quick Start](#-quick-start) · [Usage](#-usage) · [Trackers](#-tracking-algorithms) · [Evaluation](#-evaluation-metrics) · [Deployment](#-deployment)

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Key Features](#-key-features)
- [Architecture](#-architecture)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Quick Start](#-quick-start)
- [Usage](#-usage)
- [Pipeline Stages](#-pipeline-stages)
- [Tracking Algorithms](#-tracking-algorithms)
- [Evaluation Metrics](#-evaluation-metrics)
- [Configuration](#%EF%B8%8F-configuration)
- [Deployment](#-deployment)
- [Datasets](#-datasets)
- [References](#-references)
- [License](#-license)

---

## 🔍 Overview

This project implements a **real-time multi-object detection and tracking pipeline** for vehicles and pedestrians in traffic surveillance and autonomous driving scenarios. It follows a modular **Pipe-and-Filter** architecture where each processing stage (ingestion → preprocessing → detection → tracking → output) operates as an independent, swappable component.

The system combines **YOLOv8** for high-speed object detection with state-of-the-art multi-object trackers (**ByteTrack**, **DeepSORT**, **SORT**) to maintain persistent object identities across video frames — even through occlusions, re-entries, and dense traffic.

### Why This Project?

| Challenge | Solution |
|-----------|----------|
| Real-time constraint (≥30 FPS) | YOLOv8 anchor-free detector + TensorRT FP16 acceleration |
| Identity switches during occlusion | ByteTrack two-pass association (high + low confidence) |
| Class imbalance (cars ≫ pedestrians) | Focal Loss + class-aware sampling |
| Deployment reproducibility | Docker + NVIDIA Container Toolkit |
| Weather/condition overfitting | Albumentations + synthetic augmentation pipeline |

---

## ✨ Key Features

- **Multi-Detector Support** — YOLOv8 (Nano → XLarge) with seamless TensorRT engine inference
- **3 Tracking Algorithms** — ByteTrack, DeepSORT (with CNN Re-ID), and SORT baselines
- **Kalman Filter Motion Model** — 8-dimensional state vector `[cx, cy, a, h, vx, vy, va, vh]` for smooth trajectory prediction
- **Hungarian Algorithm Assignment** — Optimal bipartite matching via `scipy.linear_sum_assignment`
- **TensorRT Optimization** — FP16/INT8 quantization with up to **5× speedup** over native PyTorch
- **YAML-Driven Configuration** — Swap models, trackers, and hyperparameters without code changes
- **Comprehensive Evaluation Suite** — mAP, MOTA, MOTP, IDF1, HOTA metrics
- **Docker-Ready** — NVIDIA GPU-accelerated containers for reproducible deployments
- **CLI Interface** — Single entry point for video files, RTSP streams, and camera devices
- **Modular Design** — Each pipeline stage is independently testable and swappable

---

## 🏗 Architecture

The system follows a **Pipe-and-Filter** architecture where data flows synchronously through isolated processing nodes:

```
┌──────────────────────────────────────────────────────────────────┐
│                         PIPELINE RUNNER                          │
│                                                                  │
│  ┌─────────┐   ┌────────────┐   ┌────────┐   ┌───────┐   ┌───┐ │
│  │ Ingest  │──▶│ Preprocess │──▶│ Detect │──▶│ Track │──▶│Out│ │
│  └─────────┘   └────────────┘   └────────┘   └───────┘   └───┘ │
│   MP4/RTSP      Letterbox +      YOLOv8 /     ByteTrack   Video │
│   Camera        Normalize        TensorRT     DeepSORT    JSON  │
└──────────────────────────────────────────────────────────────────┘
```

### Tracking Node Detail

```
Tracking Node
├── Kalman Filter (Motion Model)
│   ├── Predict: Project state to next frame
│   └── Update: Incorporate matched detection
├── Cost Matrix Builder
│   ├── IoU Distance (spatial overlap)
│   └── Cosine Distance (appearance — DeepSORT only)
├── Hungarian Algorithm (Assignment)
│   ├── First Pass: High-confidence matching
│   └── Second Pass: Low-confidence recovery (ByteTrack)
└── Track Manager
    ├── Active Tracks Registry
    ├── Lost Tracks Buffer (configurable frame window)
    └── Track Deletion Logic
```

> For the full architecture document, see [`docs/architecture/ARCHITECTURE.md`](docs/architecture/ARCHITECTURE.md)

---

## 🛠 Tech Stack

| Category | Technologies |
|----------|-------------|
| **Detection** | YOLOv8 (Ultralytics), TensorRT |
| **Tracking** | ByteTrack, DeepSORT, SORT |
| **Deep Learning** | PyTorch 2.0+, TorchVision |
| **Computer Vision** | OpenCV, FFmpeg |
| **Motion Model** | FilterPy (Kalman Filter) |
| **Optimization** | SciPy (Hungarian), `lap` (fast LAP solver) |
| **Augmentation** | Albumentations, imgaug |
| **Experiment Tracking** | Weights & Biases |
| **Containerization** | Docker, NVIDIA Container Toolkit |
| **Testing** | pytest |
| **Code Quality** | Black, Flake8 |

---

## 📁 Project Structure

```
Vehicle_Pedestrian_Tracking_Research/
├── cli.py                          # Main CLI entry point
├── Makefile                        # Common project commands
├── requirements.txt                # Python dependencies
├── setup.py                        # Package installation
│
├── configs/                        # YAML configuration files
│   ├── model_config.yaml           #   YOLOv8 training & inference params
│   ├── tracker_config.yaml         #   ByteTrack / DeepSORT / SORT params
│   ├── dataset.yaml                #   Class definitions & dataset paths
│   ├── augmentation_config.yaml    #   Data augmentation pipeline
│   └── deployment_config.yaml      #   TensorRT export & edge profiles
│
├── src/                            # Core source code
│   ├── detectors/                  #   YOLOv8 & TensorRT detector wrappers
│   ├── trackers/                   #   ByteTrack, DeepSORT, SORT, Kalman Filter
│   ├── pipeline/                   #   Pipeline orchestrator & stage registry
│   ├── preprocessing/              #   Normalization, augmentation, format conversion
│   ├── evaluation/                 #   Detection & tracking metric calculators
│   ├── ingestion/                  #   Video reader & frame buffer
│   ├── visualization/              #   BBox drawing, dashboards, trajectory rendering
│   └── utils/                      #   Config loader, logging, I/O handlers
│
├── scripts/                        # Standalone utility scripts
│   ├── train_detector.py           #   YOLOv8 training launcher
│   ├── run_evaluation.py           #   Full evaluation suite
│   ├── export_tensorrt.py          #   TensorRT model export
│   ├── benchmark_fps.py            #   FPS / latency benchmarking
│   └── convert_annotations.py      #   KITTI/MOT/BDD → YOLO format
│
├── configs/                        # Experiment configurations (YAML)
├── data/                           # Raw & processed datasets
├── models/                         # Pretrained, trained, & exported weights
├── notebooks/                      # Jupyter exploration notebooks
├── outputs/                        # Logs, metrics, annotated videos
├── docker/                         # Dockerfile & docker-compose
├── tests/                          # Unit & integration tests
└── docs/                           # Architecture & research documentation
```

---

## 🚀 Quick Start

### Prerequisites

- Python ≥ 3.9
- CUDA-compatible GPU (recommended)
- [NVIDIA TensorRT](https://developer.nvidia.com/tensorrt) (optional, for accelerated inference)

### Installation

```bash
# Clone the repository
git clone https://github.com/<your-username>/Vehicle_Pedestrian_Tracking_Research.git
cd Vehicle_Pedestrian_Tracking_Research

# Create virtual environment
python -m venv venv
source venv/bin/activate        # Linux/macOS
# venv\Scripts\activate         # Windows

# Install dependencies
pip install -r requirements.txt

# Install as editable package (optional)
pip install -e .
```

### Verify Installation

```bash
make test
```

---

## 💻 Usage

### Run Tracking on a Video File

```bash
python cli.py \
    --source video.mp4 \
    --weights models/pretrained/yolov8m.pt \
    --tracker bytetrack
```

### Use TensorRT Engine with JSON Export

```bash
python cli.py \
    --source video.mp4 \
    --weights models/exported/best.engine \
    --tracker bytetrack \
    --export-json
```

### RTSP Stream with Custom Thresholds

```bash
python cli.py \
    --source rtsp://camera:554/stream \
    --conf-thresh 0.5 \
    --iou-thresh 0.5
```

### Batch Evaluation Mode

```bash
python cli.py \
    --source data/processed/test/ \
    --tracker deepsort \
    --export-json \
    --no-display
```

### Makefile Shortcuts

```bash
make train          # Train YOLOv8 on custom dataset
make eval           # Run full evaluation suite
make export         # Export model to TensorRT
make benchmark      # Run FPS/latency benchmarks
make track          # Run tracking on sample video
make docker-build   # Build production Docker image
make docker-run     # Run pipeline in Docker container
```

---

## ⚙ Pipeline Stages

| Stage | Input | Output | Key Technology |
|-------|-------|--------|----------------|
| **Ingestion** | MP4 / RTSP / Camera | Raw BGR frames (NumPy) | OpenCV `VideoCapture`, FFmpeg |
| **Preprocessing** | Raw frames | Normalized GPU tensors `[B×3×H×W]` | Letterbox resize, BGR→RGB, HWC→CHW |
| **Detection** | Preprocessed tensors | BBoxes + confidence + class logits | YOLOv8 / TensorRT engine |
| **Post-Processing** | Raw detections | Filtered `[x1, y1, x2, y2, conf, cls]` | NMS, confidence thresholding |
| **Tracking** | Filtered detections | Tracked objects with persistent IDs | Kalman Filter + Hungarian matching |
| **Output** | Tracked objects + frame | Annotated video + JSON metadata | OpenCV drawing, JSON serialization |

---

## 🎯 Tracking Algorithms

### Algorithm Comparison

| Algorithm | Speed | Occlusion Handling | Re-ID | Best For |
|-----------|-------|-------------------|-------|----------|
| **SORT** | ★★★★★ | ★★☆☆☆ | ❌ | Low-latency, sparse scenes |
| **DeepSORT** | ★★★☆☆ | ★★★★☆ | ✅ CNN embeddings | Identity-critical applications |
| **ByteTrack** | ★★★★★ | ★★★★★ | ❌ | Dense traffic, frequent occlusions |

### Primary Choice: ByteTrack

ByteTrack's **two-pass association** strategy leverages both high-confidence and low-confidence detections, recovering trajectories that single-pass methods lose during temporary occlusions. Combined with the Kalman Filter's linear motion model, it achieves state-of-the-art MOTA scores without the computational overhead of a Re-ID network.

### YOLOv8 Model Scales

| Variant | Parameters | mAP@0.5 (COCO) | FPS (T4 GPU) | Use Case |
|---------|-----------|-----------------|---------------|----------|
| YOLOv8n | 3.2M | 37.3 | 170 | Ultra-low latency edge |
| YOLOv8s | 11.2M | 44.9 | 120 | Edge deployment |
| **YOLOv8m** | **25.9M** | **50.2** | **80** | **Project baseline** |
| YOLOv8l | 43.7M | 52.9 | 50 | High-accuracy research |
| YOLOv8x | 68.2M | 53.9 | 35 | Maximum accuracy |

---

## 📊 Evaluation Metrics

### Detection Metrics
| Metric | Description |
|--------|-------------|
| **mAP@0.5** | Mean Average Precision at IoU ≥ 0.50 (standard COCO) |
| **mAP@0.5:0.95** | Mean AP across IoU thresholds 0.50–0.95 (strict) |

### Tracking Metrics
| Metric | Description |
|--------|-------------|
| **MOTA** | Multi-Object Tracking Accuracy — aggregated FN + FP + IDSW |
| **MOTP** | Multi-Object Tracking Precision — localization quality of matched tracks |
| **IDF1** | Identity F1 — measures how well correct identities are preserved |
| **HOTA** | Higher Order Tracking Accuracy — balanced detection × association |

### Performance Metrics
| Metric | Description |
|--------|-------------|
| **GPU Latency** | Per-frame inference time (ms) |
| **End-to-End FPS** | Full pipeline throughput including I/O |

---

## ⚙️ Configuration

All parameters are managed through YAML files — **no code changes needed** to swap models, trackers, or hyperparameters.

| Config File | Purpose |
|-------------|---------|
| `configs/model_config.yaml` | YOLOv8 variant, training hyperparameters, loss weights |
| `configs/tracker_config.yaml` | ByteTrack / DeepSORT / SORT parameters, Kalman Filter settings |
| `configs/dataset.yaml` | Class definitions (6 classes), dataset paths, annotation format |
| `configs/augmentation_config.yaml` | Data augmentation pipeline (Mosaic, MixUp, HSV, etc.) |
| `configs/deployment_config.yaml` | TensorRT export settings, edge device profiles (Jetson Orin) |

**Target Classes:**

| ID | Class |
|----|-------|
| 0 | Person |
| 1 | Car |
| 2 | Truck |
| 3 | Bus |
| 4 | Motorcycle |
| 5 | Bicycle |

---

## 🐳 Deployment

### Docker

```bash
# Build production image (NVIDIA GPU base)
docker build -f docker/Dockerfile -t vehicle-tracker:latest .

# Run with GPU passthrough
docker run --gpus all \
    -v $(pwd)/data:/app/data \
    -v $(pwd)/outputs:/app/outputs \
    vehicle-tracker:latest \
    --source /app/data/raw/sample.mp4
```

### TensorRT Optimization

```bash
# Export PyTorch model → TensorRT FP16 engine
python scripts/export_tensorrt.py --config configs/deployment_config.yaml

# Benchmark accelerated inference
python scripts/benchmark_fps.py \
    --source data/raw/sample.mp4 \
    --weights models/exported/best.engine
```

### Edge Deployment Profiles

| Device | Resolution | Precision | Target FPS |
|--------|-----------|-----------|------------|
| Jetson Orin NX (25W) | 640×640 | FP16 | 30 |
| Jetson AGX Orin (60W) | 1280×1280 | FP16 | 60 |

---

## 📚 Datasets

| Dataset | Volume | Key Classes | Format |
|---------|--------|-------------|--------|
| **KITTI** | 7,481 frames | Car, Pedestrian, Cyclist | Custom TXT → YOLO |
| **MOT17/20** | Multi-sequence | Pedestrian (primary) | CSV → YOLO |
| **BDD100K** | 100K videos | Person, Car, Truck, Bus, Bike | COCO JSON → YOLO |
| **Waymo Open** | 103K segments | Vehicle, Pedestrian, Cyclist | TFRecord → YOLO |

All annotations are converted to YOLO format (`class_id cx cy w h`, normalized 0–1) using the conversion script:

```bash
python scripts/convert_annotations.py
```

---

## 📖 References

1. **YOLOv8** — Ultralytics Documentation
2. **ByteTrack** — *Multi-Object Tracking by Associating Every Detection Box* (Zhang et al.)
3. **DeepSORT** — *Simple Online and Realtime Tracking with a Deep Association Metric* (Wojke et al.)
4. **HOTA** — *A Higher Order Metric for Evaluating Multi-Object Tracking* (Luiten et al.)
5. **BDD100K** — *A Diverse Driving Dataset for Heterogeneous Multitask Learning* (Yu et al., CVPR 2020)
6. **Waymo Open Dataset** (Sun et al.)
7. **KITTI Vision Benchmark Suite** (Geiger et al.)

> Full literature review available in [`docs/research/RESEARCH_NOTES.md`](docs/research/RESEARCH_NOTES.md)

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

**Built with** ❤️ **for computer vision research**

</div>
