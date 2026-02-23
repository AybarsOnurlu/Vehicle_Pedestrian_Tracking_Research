"""
Command-Line Interface for Vehicle & Pedestrian Tracking System.

Entry point for running the detection + tracking pipeline.

Usage Examples:
    # Run tracking on a video file
    python cli.py --source video.mp4 --weights models/pretrained/yolov8m.pt --tracker bytetrack

    # Use TensorRT engine with JSON export
    python cli.py --source video.mp4 --weights models/exported/best.engine --tracker bytetrack --export-json

    # RTSP stream with custom thresholds
    python cli.py --source rtsp://camera:554/stream --conf-thresh 0.5 --iou-thresh 0.5

    # Batch evaluation mode
    python cli.py --source data/processed/test/ --tracker deepsort --export-json --no-display
"""
