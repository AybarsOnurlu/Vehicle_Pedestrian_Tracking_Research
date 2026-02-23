"""
Preprocessing Module
====================

Data preparation for both training and inference pipelines.

Key Components:
    - FormatConverter: Converts annotations across dataset formats (MOT, KITTI, COCO → YOLO)
    - Augmentation: Road-scene specific data augmentation (weather, sensor degradation)
    - Normalizer: Tensor normalization, resizing, and GPU transfer

Supported Conversions:
    MOT CSV → YOLO TXT
    KITTI TXT → YOLO TXT
    COCO JSON → YOLO TXT
    Waymo TFRecord → YOLO TXT
"""
