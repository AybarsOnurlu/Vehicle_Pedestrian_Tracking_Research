# Makefile for common project operations
# Usage: make <target>

.PHONY: help install train eval export benchmark docker-build docker-run clean

help:  ## Show this help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

install:  ## Install Python dependencies
	pip install -r requirements.txt

train:  ## Train YOLOv8 model on custom dataset
	python scripts/train_detector.py --config configs/model_config.yaml

eval:  ## Run full evaluation suite (detection + tracking metrics)
	python scripts/run_evaluation.py --config configs/dataset.yaml

export:  ## Export model to TensorRT format
	python scripts/export_tensorrt.py --config configs/deployment_config.yaml

benchmark:  ## Run FPS/latency benchmarks
	python scripts/benchmark_fps.py --source data/raw/sample.mp4 --weights models/exported/best.engine

track:  ## Run tracking pipeline on sample video
	python cli.py --source data/raw/sample.mp4 --weights models/pretrained/yolov8m.pt --tracker bytetrack --export-json

docker-build:  ## Build production Docker image
	docker build -f docker/Dockerfile -t vehicle-tracker:latest .

docker-run:  ## Run tracking pipeline in Docker container
	docker run --gpus all -v $(PWD)/data:/app/data -v $(PWD)/outputs:/app/outputs vehicle-tracker:latest --source /app/data/raw/sample.mp4

test:  ## Run unit tests
	pytest tests/ -v

clean:  ## Remove cached files and outputs
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	rm -rf outputs/videos/* outputs/logs/* outputs/metrics/*
