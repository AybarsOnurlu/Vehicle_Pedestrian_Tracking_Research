"""
Video Ingestion Module
======================

Handles video source management for the tracking pipeline.

Supported sources:
    - Local video files (MP4, AVI, MKV)
    - RTSP network streams
    - Direct camera feeds (USB, CSI)

Key Components:
    - VideoReader: OpenCV-based frame decoder with FFmpeg backend
    - FrameBuffer: Thread-safe queue for decoupled frame production/consumption

Usage:
    reader = VideoReader(source="video.mp4", target_fps=30)
    for frame in reader:
        process(frame)
"""
