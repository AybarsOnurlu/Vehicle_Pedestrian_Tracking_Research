"""
Batch Annotation Format Conversion Script.

Converts dataset-specific annotation formats into unified YOLO format
for training. Supports KITTI, MOT, COCO, and BDD100K source formats.

Output Format (YOLO):
    class_id center_x center_y width height
    (all values normalized 0.0–1.0 relative to image dimensions)

Usage:
    python scripts/convert_annotations.py \
        --source data/raw/kitti/ \
        --format kitti \
        --output data/processed/train/labels/

    python scripts/convert_annotations.py \
        --source data/raw/bdd100k/ \
        --format bdd100k \
        --output data/processed/train/labels/

Supported Formats:
    kitti   → KITTI TXT (15-column)
    mot     → MOTChallenge CSV (gt.txt)
    coco    → COCO JSON (instances_*.json)
    bdd100k → BDD100K JSON (bdd100k_labels_*.json)
"""

# TODO: Implement conversion logic using src.preprocessing.format_converter
