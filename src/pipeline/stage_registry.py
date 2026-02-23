"""
StageRegistry - Dynamic pipeline stage loader.

Enables runtime selection of detector and tracker implementations
based on configuration files, supporting hot-swap without code changes.

Public API:
    class StageRegistry:
        @staticmethod
        def get_detector(config: dict) -> BaseDetector
        
        @staticmethod
        def get_tracker(config: dict) -> BaseTracker
"""
