"""
Detectors Module
================

Object detection engines for the tracking pipeline.

Implements a strategy pattern with swappable detector backends:
    - YOLODetector: Native PyTorch YOLOv8 inference
    - TensorRTDetector: Optimized TensorRT engine inference

All detectors conform to BaseDetector interface for pipeline compatibility.
"""
