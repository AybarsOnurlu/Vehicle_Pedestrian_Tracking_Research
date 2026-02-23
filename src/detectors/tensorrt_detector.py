"""
TensorRTDetector - Optimized inference via NVIDIA TensorRT.

Benefits over native PyTorch:
    - Layer fusion & kernel auto-tuning
    - FP16/INT8 quantization (up to 5x speedup)
    - Eliminates Python GIL bottleneck for inference
    - Essential for edge deployment (Jetson Orin)

Public API:
    class TensorRTDetector(BaseDetector):
        def __init__(self, engine_path: str, conf_thresh: float, iou_thresh: float)
        def detect(self, frame: np.ndarray) -> List[Detection]
        def warmup(self) -> None
        def get_latency(self) -> float
"""
