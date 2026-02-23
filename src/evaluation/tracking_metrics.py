"""
TrackingMetrics - Multi-Object Tracking evaluation.

Metrics (via TrackEval library):
    - MOTA: Multiple Object Tracking Accuracy (FN + FP + IDSW)
    - MOTP: Multiple Object Tracking Precision (localization quality)
    - IDF1: Identity F1-Score (identity preservation duration)
    - HOTA: Higher Order Tracking Accuracy (balanced DetA × AssA)
    - ID Switches count
    - Track fragmentation count

Public API:
    class TrackingMetrics:
        def __init__(self, predictions_path: str, ground_truth_path: str, dataset_format: str)
        def compute_clear_mot(self) -> dict
        def compute_hota(self) -> dict
        def compute_identity(self) -> dict
        def export_report(self, output_path: str) -> None
"""
