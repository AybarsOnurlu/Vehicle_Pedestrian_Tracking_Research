"""
FrameBuffer - Thread-safe frame queue for pipeline decoupling.

Responsibilities:
    - Buffered frame storage between ingestion and processing stages
    - Configurable queue depth to balance latency vs memory
    - Drop-oldest policy when queue is full (real-time mode)

Public API:
    class FrameBuffer:
        def __init__(self, max_size: int = 128)
        def put(self, frame: np.ndarray, metadata: dict) -> None
        def get(self, timeout: float = 1.0) -> Tuple[np.ndarray, dict]
        def is_empty(self) -> bool
"""
