"""
BaseDetector - Abstract interface for all detection engines.

Ensures pipeline compatibility regardless of the detection backend.

Public API:
    class BaseDetector(ABC):
        @abstractmethod
        def __init__(self, weights_path: str, config: dict)
        
        @abstractmethod
        def detect(self, frame: np.ndarray) -> List[Detection]
            '''Returns list of Detection(x1, y1, x2, y2, confidence, class_id)'''
        
        @abstractmethod
        def warmup(self) -> None
            '''Run dummy inference to initialize GPU kernels'''
        
        @abstractmethod
        def get_latency(self) -> float
            '''Returns last inference latency in milliseconds'''
"""
