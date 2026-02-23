"""
Evaluation Module
=================

Quantitative assessment of detection and tracking performance.

Components:
    - DetectionMetrics: mAP@0.5, mAP@0.5:0.95 (COCO standard)
    - TrackingMetrics: MOTA, MOTP, IDF1, HOTA (via TrackEval)
    - SpeedBenchmark: FPS profiling, GPU latency measurement
"""
