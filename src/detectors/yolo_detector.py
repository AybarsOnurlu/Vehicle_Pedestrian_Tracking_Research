"""
YOLODetector - YOLOv8 PyTorch inference engine.

Wraps Ultralytics YOLO for object detection with:
    - Pre-trained or fine-tuned weight loading
    - Configurable confidence and NMS thresholds
    - Multi-class filtering (vehicles, pedestrians)
    - FP16 half-precision support

Public API:
    class YOLODetector(BaseDetector):
        def __init__(self, weights_path: str, conf_thresh: float, iou_thresh: float, device: str)
        def detect(self, frame: np.ndarray) -> List[Detection]
        def warmup(self) -> None
        def get_latency(self) -> float
"""
