"""
KalmanFilter - 8-dimensional state estimation for bounding box tracking.

State Vector: [cx, cy, aspect_ratio, height, v_cx, v_cy, v_a, v_h]
    - (cx, cy): Bounding box center coordinates
    - aspect_ratio: Width / Height ratio
    - height: Bounding box height
    - v_*: Respective velocities (constant-velocity assumption)

Measurement Vector: [cx, cy, aspect_ratio, height]

Operations:
    1. Predict: Project state forward using state transition matrix (F)
    2. Update: Incorporate new detection measurement to refine state estimate

Variants:
    - Standard Linear Kalman Filter (default)
    - NSA (Noise Scale Adaptive) Kalman Filter for nonlinear motion

Public API:
    class KalmanBoxTracker:
        def __init__(self, bbox: np.ndarray)
        def predict(self) -> np.ndarray
        def update(self, bbox: np.ndarray) -> None
        def get_state(self) -> np.ndarray
"""
