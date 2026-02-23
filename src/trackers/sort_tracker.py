"""
SORTTracker - Simple Online and Realtime Tracking.

Algorithm:
    1. Kalman Filter predicts next position for each active track
    2. IoU cost matrix computed between predictions and new detections
    3. Hungarian algorithm finds optimal assignment
    4. Matched tracks updated; unmatched detections become new tracks
    5. Unmatched tracks aged and deleted after max_age frames

Properties:
    - Extremely fast (minimal computational overhead)
    - No visual appearance features (IoU-only matching)
    - High ID switch rate during occlusion

Public API:
    class SORTTracker(BaseTracker):
        def __init__(self, max_age=1, min_hits=3, iou_threshold=0.3)
        def update(self, detections, frame) -> List[Track]
"""
