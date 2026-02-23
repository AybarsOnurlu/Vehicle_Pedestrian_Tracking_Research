"""
Trackers Module
===============

Multi-Object Tracking (MOT) algorithms for temporal identity association.

Available Trackers:
    - SORTTracker: Kalman Filter + Hungarian (IoU-only) — fastest, basic
    - DeepSORTTracker: + CNN Re-ID appearance embeddings — best identity preservation
    - ByteTracker: Two-pass association with low-confidence recovery — best occlusion handling

All trackers conform to BaseTracker interface.
"""
