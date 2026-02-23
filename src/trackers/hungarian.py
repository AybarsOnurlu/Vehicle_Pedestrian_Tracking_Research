"""
Hungarian Algorithm - Optimal bipartite matching wrapper.

Wraps scipy.optimize.linear_sum_assignment for O(n^3) optimal assignment
between predicted track positions and new detections.

Cost Matrix Options:
    - IoU Distance: 1 - IoU(predicted_bbox, detected_bbox)
    - Mahalanobis Distance: Statistical distance from Kalman state
    - Cosine Distance: Appearance embedding similarity (DeepSORT)

Public API:
    def compute_iou_cost_matrix(tracks, detections) -> np.ndarray
    def compute_cosine_cost_matrix(track_features, detection_features) -> np.ndarray
    def linear_assignment(cost_matrix, threshold) -> Tuple[matches, unmatched_tracks, unmatched_detections]
"""
