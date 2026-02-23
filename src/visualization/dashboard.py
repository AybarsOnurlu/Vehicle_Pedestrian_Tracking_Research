"""
Dashboard - Real-time metrics overlay on output frames.

Displays:
    - Current FPS
    - Active / Lost / Total track counts
    - Per-class detection counts
    - GPU memory usage

Public API:
    class Dashboard:
        def __init__(self, position: str = "top-left")
        def render(self, frame: np.ndarray, metrics: dict) -> np.ndarray
"""
