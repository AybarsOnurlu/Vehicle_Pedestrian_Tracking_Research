"""
BaseTracker - Abstract interface for all tracking algorithms.

Public API:
    class BaseTracker(ABC):
        @abstractmethod
        def __init__(self, config: dict)
        
        @abstractmethod
        def update(self, detections: List[Detection], frame: np.ndarray) -> List[Track]
            '''Associate detections to tracks, return updated track list.
            Each Track contains: track_id, bbox, class_id, age, state'''
        
        @abstractmethod
        def get_active_tracks(self) -> List[Track]
            '''Return currently active (confirmed) tracks'''
        
        @abstractmethod
        def get_lost_tracks(self) -> List[Track]
            '''Return tracks in lost/buffered state'''
        
        @abstractmethod
        def reset(self) -> None
            '''Clear all tracks and reset state'''
"""
