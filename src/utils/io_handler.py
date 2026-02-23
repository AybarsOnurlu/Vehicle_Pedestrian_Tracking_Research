"""
IOHandler - Tracking metadata serialization.

Exports per-frame tracking results in structured formats:
    - JSON: Full metadata with nested track objects
    - CSV: Flat tabular format compatible with TrackEval

Schema:
    {
        "frame_id": int,
        "timestamp": float,
        "tracks": [
            {"track_id": int, "class": str, "bbox": [x1, y1, x2, y2], "confidence": float}
        ]
    }

Public API:
    class IOHandler:
        def __init__(self, output_path: str, format: str = "json")
        def write_frame(self, frame_id: int, tracks: List[Track]) -> None
        def finalize(self) -> None
"""
