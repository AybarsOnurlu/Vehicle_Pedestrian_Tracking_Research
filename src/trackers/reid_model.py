"""
ReIDModel - Appearance feature extractor for DeepSORT.

Extracts visual feature embeddings from cropped bounding box images
using a lightweight CNN backbone trained with triplet loss.

Architecture Options:
    - OSNet (Omni-Scale Network) — lightweight, strong re-id performance
    - ResNet-18 backbone with modified final layers
    - MobileNetV2 for edge deployment

Public API:
    class ReIDModel:
        def __init__(self, checkpoint_path: str, device: str = "cuda:0")
        def extract_features(self, image_crops: List[np.ndarray]) -> np.ndarray
            '''Returns NxD feature matrix (D=128/256/512 depending on backbone)'''
"""
