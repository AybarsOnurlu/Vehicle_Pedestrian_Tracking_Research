"""
Hardware Speed Benchmarking Script.

Profiles end-to-end pipeline throughput and per-stage latency
across different model variants and hardware configurations.

Benchmark Metrics:
    - End-to-End FPS (frames per second)
    - Detection inference latency (ms)
    - Tracking update latency (ms)
    - GPU memory utilization
    - Preprocessing overhead

Usage:
    python scripts/benchmark_fps.py \
        --source data/raw/sample.mp4 \
        --weights models/exported/best.engine

    python scripts/benchmark_fps.py \
        --source data/raw/sample.mp4 \
        --weights models/pretrained/yolov8m.pt \
        --warmup 50 \
        --iterations 500
"""

# TODO: Implement benchmarking loop using src.evaluation.speed_benchmark
# from src.evaluation.speed_benchmark import FPSBenchmark
