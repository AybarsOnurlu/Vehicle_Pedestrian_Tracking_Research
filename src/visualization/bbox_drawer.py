"""
BBoxDrawer - Bounding box and ID annotation renderer.

Public API:
    class BBoxDrawer:
        def __init__(self, class_colors: dict = None, thickness: int = 2)
        def draw(self, frame: np.ndarray, tracks: List[Track]) -> np.ndarray
"""
