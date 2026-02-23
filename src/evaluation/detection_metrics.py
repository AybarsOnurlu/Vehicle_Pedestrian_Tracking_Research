"""
DetectionMetrics - COCO-standard detection evaluation.

Metrics:
    - mAP@0.5: Mean AP at IoU=0.50 threshold
    - mAP@0.5:0.95: Mean AP averaged over IoU thresholds [0.50, 0.55, ..., 0.95]
    - Per-class AP breakdown
    - Precision-Recall curves

Public API:
    class DetectionMetrics:
        def __init__(self, predictions_path: str, ground_truth_path: str)
        def compute(self) -> dict
        def export_report(self, output_path: str) -> None
"""
