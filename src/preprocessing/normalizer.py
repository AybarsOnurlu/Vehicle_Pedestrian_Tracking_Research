"""
Normalizer - Frame preprocessing for model inference.

Responsibilities:
    - Letterbox resize to model input dimensions (640/1280)
    - Pixel normalization (0-255 → 0.0-1.0)
    - BGR → RGB color space conversion
    - HWC → CHW tensor transpose
    - GPU tensor transfer (CUDA)
    - Optional batch assembly

Public API:
    class FrameNormalizer:
        def __init__(self, target_size: int = 1280, device: str = "cuda:0")
        def preprocess(self, frame: np.ndarray) -> torch.Tensor
        def preprocess_batch(self, frames: List[np.ndarray]) -> torch.Tensor
"""
