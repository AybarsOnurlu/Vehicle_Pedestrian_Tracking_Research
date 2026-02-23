"""
DeepSORTTracker - Deep SORT with Re-Identification embeddings.

Extension of SORT that adds:
    - CNN-based appearance feature extraction (Re-ID model)
    - Cosine distance matching for visual similarity
    - Weighted fusion: λ * appearance_cost + (1-λ) * motion_cost
    - Feature gallery per track (nn_budget recent embeddings)

Algorithm:
    1. Kalman predict → state projection
    2. Extract Re-ID embeddings from detected bounding box crops
    3. Build cost matrix: Mahalanobis (motion) + Cosine (appearance)
    4. Cascade matching: prioritize recently seen tracks
    5. Hungarian assignment with gating thresholds
    6. IOU-based fallback for remaining unmatched

Public API:
    class DeepSORTTracker(BaseTracker):
        def __init__(self, reid_model_path, max_cosine_dist, max_age, n_init, nn_budget)
        def update(self, detections, frame) -> List[Track]
"""
