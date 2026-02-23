#!/bin/bash
# ============================================
# Dataset Download Script
# Vehicle & Pedestrian Tracking Project
# ============================================
# Downloads and organizes raw datasets for training.
#
# Supported Datasets:
#   - BDD100K (Berkeley DeepDrive)
#   - KITTI Object Detection
#   - MOT17 Challenge
#   - Waymo Open Dataset (requires gcloud CLI)
#
# Usage:
#   chmod +x scripts/download_datasets.sh
#   ./scripts/download_datasets.sh --dataset bdd100k --output data/raw/
#
# Prerequisites:
#   - wget, unzip, tar
#   - gcloud CLI (Waymo only)
#   - Registered API keys (see docs/research/RESEARCH_NOTES.md)
# ============================================

set -euo pipefail

DATASET=${1:-"all"}
OUTPUT_DIR=${2:-"data/raw"}

echo "============================================"
echo " Dataset Downloader"
echo " Target: ${DATASET}"
echo " Output: ${OUTPUT_DIR}"
echo "============================================"

# TODO: Implement dataset-specific download logic
# - BDD100K: https://bdd-data.berkeley.edu/
# - KITTI: https://www.cvlibs.net/datasets/kitti/
# - MOT17: https://motchallenge.net/
# - Waymo: https://waymo.com/open/

echo "[INFO] Dataset download script ready for implementation."
