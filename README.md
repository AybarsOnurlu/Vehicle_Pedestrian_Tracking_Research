# Vehicle & Pedestrian Detection + Tracking

A modular detection and tracking pipeline for vehicles and pedestrians in video. Built with **YOLOv8** + **ByteTrack**, designed to be extended iteratively.

<!-- TODO: Add a short demo GIF here once a working prototype is ready -->
<!-- ![Demo](assets/demo.gif) -->

---

## What It Does

1. **Reads** video input (MP4 file, RTSP stream, or webcam)
2. **Detects** vehicles & pedestrians per frame using YOLOv8
3. **Tracks** objects across frames with persistent IDs (ByteTrack or DeepSORT)
4. **Outputs** annotated video + optional JSON metadata

```
Video Input → YOLOv8 Detection → ByteTrack Tracking → Annotated Output
```

---

## Supported Classes

| ID | Class |
|----|-------|
| 0 | Person |
| 1 | Car |
| 2 | Truck |
| 3 | Bus |
| 4 | Motorcycle |
| 5 | Bicycle |

---

## Quick Start

```bash
# Clone
git clone https://github.com/AybarsOnurlu/Vehicle_Pedestrian_Tracking_Research.git
cd Vehicle_Pedestrian_Tracking_Research

# Setup
python -m venv venv
source venv/bin/activate        # Linux/macOS
# venv\Scripts\activate         # Windows
pip install -r requirements.txt

# Run
python cli.py --source video.mp4 --weights models/pretrained/yolov8m.pt --tracker bytetrack
```

---

## Usage Examples

```bash
# Basic tracking
python cli.py --source video.mp4 --weights models/pretrained/yolov8m.pt --tracker bytetrack

# With JSON export
python cli.py --source video.mp4 --tracker bytetrack --export-json

# RTSP stream
python cli.py --source rtsp://camera:554/stream --conf-thresh 0.5

# DeepSORT (appearance-based re-ID)
python cli.py --source video.mp4 --tracker deepsort
```

---

## Project Structure

```
├── cli.py                      # CLI entry point
├── configs/
│   ├── model_config.yaml       # YOLOv8 training & inference settings
│   ├── tracker_config.yaml     # ByteTrack / DeepSORT parameters
│   └── dataset.yaml            # Class definitions & dataset paths
│
├── src/
│   ├── detectors/              # YOLOv8 detector wrapper
│   ├── trackers/               # ByteTrack, DeepSORT, SORT + Kalman Filter
│   ├── pipeline/               # Main processing loop
│   ├── preprocessing/          # Resize, normalize, format conversion
│   ├── evaluation/             # MOTA, IDF1, mAP metric calculators
│   ├── ingestion/              # Video reader
│   ├── visualization/          # BBox drawing, trajectory rendering
│   └── utils/                  # Config loader, logging, I/O
│
├── scripts/                    # Train, evaluate, convert annotations
├── tests/                      # Unit tests
├── data/                       # Raw & processed datasets (not tracked by git)
├── models/                     # Weights (not tracked by git)
└── outputs/                    # Results, logs, annotated videos
```

---

## How Tracking Works

The pipeline follows a **tracking-by-detection** approach:

1. **YOLOv8** detects objects each frame → `[x1, y1, x2, y2, confidence, class]`
2. **Kalman Filter** predicts where existing tracks should be
3. **Hungarian Algorithm** matches new detections to predicted tracks (IoU-based)
4. **ByteTrack's two-pass matching** recovers low-confidence detections that single-pass methods miss — this is what prevents ID switches during temporary occlusions

```
Detections ──┬── High-confidence match (first pass)
             └── Low-confidence recovery (second pass) ── Updated Tracks
```

**DeepSORT** is also available when appearance-based re-identification is needed (e.g., objects that look different from each other).

---

## Tracker Options

| Tracker | Strengths | When to Use |
|---------|-----------|-------------|
| **ByteTrack** | Fast, handles occlusions well | Default — best for most traffic scenes |
| **DeepSORT** | Uses appearance features for re-ID | When objects frequently disappear and reappear |
| **SORT** | Very fast, minimal | Simple scenes, low-latency requirement |

---

## Evaluation

Standard MOT (Multi-Object Tracking) metrics:

| Metric | What It Measures |
|--------|-----------------|
| **MOTA** | Overall tracking accuracy (missed + false + ID switches) |
| **IDF1** | How well identities are preserved over time |
| **mAP@0.5** | Detection accuracy |

```bash
python scripts/run_evaluation.py --config configs/dataset.yaml
```

---

## Configuration

All settings are in YAML files — no code changes needed:

- `configs/model_config.yaml` — YOLOv8 model variant, confidence threshold, image size
- `configs/tracker_config.yaml` — Tracker parameters (thresholds, buffer size, Kalman settings)
- `configs/dataset.yaml` — Class names, dataset paths

---

## Roadmap

- [x] Project architecture & module design
- [x] Configuration system (YAML-driven)
- [ ] Core detection + tracking pipeline (MVP)
- [ ] Evaluation on KITTI / MOT17 benchmarks
- [ ] Performance optimization (speed/accuracy tuning)

---

## Tech Stack

| | |
|---|---|
| Detection | YOLOv8 (Ultralytics) |
| Tracking | ByteTrack, DeepSORT, SORT |
| Motion Model | Kalman Filter (FilterPy) |
| Assignment | Hungarian Algorithm (SciPy) |
| Video I/O | OpenCV |
| Config | YAML |
| Testing | pytest |

---

## References

- [YOLOv8 — Ultralytics](https://docs.ultralytics.com)
- [ByteTrack — Zhang et al.](https://arxiv.org/abs/2110.06864)
- [DeepSORT — Wojke et al.](https://arxiv.org/abs/1703.07402)

> Detailed literature review: [`docs/research/RESEARCH_NOTES.md`](docs/research/RESEARCH_NOTES.md)
> Architecture design: [`docs/architecture/ARCHITECTURE.md`](docs/architecture/ARCHITECTURE.md)

---

## License

MIT — see [LICENSE](LICENSE)
