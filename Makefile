# Makefile for common project operations
# Usage: make <target>

.PHONY: help install train eval track test clean

help:  ## Show this help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install:  ## Install Python dependencies
	pip install -r requirements.txt

train:  ## Train YOLOv8 model on custom dataset
	python scripts/train_detector.py --config configs/model_config.yaml

eval:  ## Run full evaluation suite (detection + tracking metrics)
	python scripts/run_evaluation.py --config configs/dataset.yaml

track:  ## Run tracking pipeline on sample video
	python cli.py --source data/raw/sample.mp4 --weights models/pretrained/yolov8m.pt --tracker bytetrack --export-json

test:  ## Run unit tests
	pytest tests/ -v

clean:  ## Remove cached files and outputs
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	rm -rf outputs/videos/* outputs/logs/* outputs/metrics/*
