"""
Full Evaluation Suite Runner.

Computes detection and tracking metrics against ground truth annotations.

Detection Metrics:
    - mAP@0.5: Mean Average Precision at IoU 0.50
    - mAP@0.5:0.95: Mean AP averaged over IoU thresholds 0.50–0.95

Tracking Metrics (via TrackEval):
    - MOTA: Multi-Object Tracking Accuracy
    - MOTP: Multi-Object Tracking Precision
    - IDF1: ID F1-Score (identity preservation)
    - HOTA: Higher Order Tracking Accuracy

Usage:
    python scripts/run_evaluation.py \
        --config configs/dataset.yaml

    python scripts/run_evaluation.py \
        --predictions outputs/metrics/tracks.json \
        --gt data/processed/test/labels/ \
        --metrics mota,idf1,hota
"""

# TODO: Implement evaluation pipeline using src.evaluation modules
# from src.evaluation.detection_metrics import compute_map
# from src.evaluation.tracking_metrics import compute_mot_metrics
