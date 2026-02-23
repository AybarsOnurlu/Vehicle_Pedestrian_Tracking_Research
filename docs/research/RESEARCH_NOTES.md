# Research Notes & Literature Review
## Vehicle & Pedestrian Detection and Tracking

---

## 1. Object Detection — One-Stage vs Two-Stage

### Two-Stage Detectors (Faster R-CNN Family)
- **Mechanism**: Decoupled localization → Region Proposal Network (RPN) generates candidate boxes → RoI Align pools features → classification + regression
- **Strengths**: Exceptional accuracy for small objects (distant pedestrians), high noise resilience
- **Weaknesses**: Computationally expensive; <30 FPS on most hardware; unsuitable for real-time edge deployment

### One-Stage Detectors
- **SSD**: Multi-scale feature maps for varying object sizes; struggles with small objects
- **RetinaNet**: Introduced **Focal Loss** — down-weights easy negatives, forces focus on hard (occluded) targets
- **YOLOv8** (Selected): Anchor-free design, decoupled classification/regression head, advanced feature pyramids
  - mAP superiority over Faster R-CNN at dramatically lower GPU latency
  - Multiple scales available (Nano → XLarge)

### Decision: **YOLOv8m** for prototype — optimal accuracy/speed balance for real-time tracking

---

## 2. Multi-Object Tracking (MOT) Algorithms

### Tracking-by-Detection (TBD) Paradigm
Two discrete steps: (1) detect objects per-frame, (2) associate detections to trajectories via spatial/temporal heuristics.

### Algorithm Evolution

| Algorithm | Innovation | Limitation |
|-----------|-----------|------------|
| **SORT** | Kalman Filter + Hungarian on IoU | High ID switches during occlusion |
| **DeepSORT** | + CNN Re-ID embeddings (Cosine distance) | Re-ID model adds inference latency |
| **ByteTrack** | Two-pass matching; retains low-confidence detections | No visual Re-ID (spatial only) |
| **FairMOT** | Joint Detection + Embedding (anchor-free, parallel Re-ID branch) | Training complexity |

### Decision: **ByteTrack + YOLOv8** — SOTA trajectory preservation without Re-ID bottleneck

---

## 3. Datasets Summary

| Dataset | Volume | Key Classes | Format | License |
|---------|--------|-------------|--------|---------|
| KITTI | 7,481 frames | Car, Pedestrian, Cyclist | Custom TXT | CC BY-NC-SA 3.0 |
| MOT17/20 | Multi-sequence | Pedestrian (primary) | CSV | CC BY-NC-SA 3.0 |
| BDD100K | 100K videos, 30fps | Person, Car, Truck, Bus, Bike | COCO JSON | BSD-3 |
| Waymo Open | 103K segments | Vehicle, Pedestrian, Cyclist | TFRecord | Non-Commercial |

All converted to YOLO format: `class_id cx cy w h` (normalized 0–1)

---

## 4. Key Technical Challenges & Mitigations

1. **Class Imbalance**: Cars vastly outnumber pedestrians → Focal Loss + class-aware sampling
2. **Annotation Jitter**: Noisy labels → EMA smoothing on bbox outputs before Kalman ingestion
3. **Weather Overfitting**: Train on clear-day only → fails in rain/fog → mandatory synthetic augmentation
4. **Re-ID Contamination**: Identical-looking vehicles swap IDs → dynamic IoU/appearance cost weighting

---

## 5. Evaluation Metrics

- **mAP@0.5 / mAP@0.5:0.95** — Detection accuracy (COCO standard)
- **MOTA** — Tracking accuracy (FN + FP + IDSW normalized)
- **MOTP** — Localization precision of matched tracks
- **IDF1** — Identity preservation quality (correct ID duration)
- **HOTA** — Modern balanced metric (Detection Accuracy × Association Accuracy)

---

## 6. Key References

1. YOLOv8 Architecture — Ultralytics Documentation
2. ByteTrack: Multi-Object Tracking by Associating Every Detection Box (Zhang et al.)
3. Deep SORT: Simple Online and Realtime Tracking with a Deep Association Metric (Wojke et al.)
4. HOTA: A Higher Order Metric for Evaluating Multi-Object Tracking (Luiten et al.)
5. BDD100K: A Diverse Driving Dataset for Heterogeneous Multitask Learning (Yu et al., CVPR 2020)
6. Waymo Open Dataset (Sun et al.)
7. KITTI Vision Benchmark Suite (Geiger et al.)
