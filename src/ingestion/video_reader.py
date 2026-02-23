"""
VideoReader - Frame extraction from video sources.

Responsibilities:
    - Decode video frames via OpenCV VideoCapture (FFmpeg backend)
    - Handle RTSP reconnection on stream failures
    - Expose frame metadata (timestamp, resolution, frame_id)
    - Optional hardware-accelerated decoding (CUDA, VAAPI)

Public API:
    class VideoReader:
        def __init__(self, source: str, target_fps: int = 30)
        def __iter__(self) -> Iterator[np.ndarray]
        def get_metadata(self) -> dict
        def release(self) -> None
"""
