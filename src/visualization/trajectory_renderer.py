"""
TrajectoryRenderer - Motion trail visualization.

Draws the historical path of each tracked object as a fading
polyline behind the current bounding box position.

Public API:
    class TrajectoryRenderer:
        def __init__(self, trail_length: int = 30, fade: bool = True)
        def draw_trails(self, frame: np.ndarray, tracks: List[Track]) -> np.ndarray
"""
