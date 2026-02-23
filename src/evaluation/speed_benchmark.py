"""
SpeedBenchmark - Performance profiling and latency measurement.

Metrics:
    - Per-frame GPU inference latency (ms)
    - End-to-end pipeline FPS (including decode, preprocess, track, render)
    - Component-wise latency breakdown
    - Warmup exclusion for accurate measurement

Public API:
    class SpeedBenchmark:
        def __init__(self, pipeline_runner: PipelineRunner, num_frames: int = 500)
        def run(self) -> dict
        def export_report(self, output_path: str) -> None
"""
