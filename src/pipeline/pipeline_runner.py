"""
PipelineRunner - Main execution orchestrator.

Connects all pipeline stages into a coherent processing loop:
    1. Initialize video source (Ingestion)
    2. Load detector model (YOLOv8 / TensorRT)
    3. Initialize tracker (ByteTrack / DeepSORT / SORT)
    4. Frame loop: Read → Preprocess → Detect → Track → Render → Export
    5. Compute and report FPS / latency metrics

Supports:
    - Live video with real-time display
    - Batch processing of pre-recorded footage
    - JSON/CSV metadata export alongside annotated video

Public API:
    class PipelineRunner:
        def __init__(self, source, weights, tracker_type, conf_thresh, iou_thresh, export_json)
        def execute(self) -> None
        def get_summary(self) -> dict
"""
