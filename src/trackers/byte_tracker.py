"""
ByteTracker - ByteTrack two-pass association algorithm.

Key Innovation: Retains low-confidence detections for second-pass matching,
recovering partially occluded targets that traditional trackers discard.

Algorithm:
    FIRST PASS (High-Confidence):
        1. Filter detections: score > track_high_thresh
        2. Kalman predict for all active tracks
        3. Hungarian matching (IoU cost) between tracks and high-conf detections
        4. Update matched tracks; collect unmatched tracks and detections
    
    SECOND PASS (Low-Confidence Recovery):
        5. Filter remaining detections: track_low_thresh < score < track_high_thresh
        6. Hungarian matching (IoU cost) between unmatched tracks and low-conf detections
        7. Recovered tracks updated; still-unmatched tracks enter lost buffer
    
    TRACK LIFECYCLE:
        8. Unmatched high-conf detections → new track candidates
        9. Lost tracks held for track_buffer frames before permanent deletion

Public API:
    class ByteTracker(BaseTracker):
        def __init__(self, track_high_thresh, track_low_thresh, match_thresh, track_buffer)
        def update(self, detections, frame) -> List[Track]
"""
