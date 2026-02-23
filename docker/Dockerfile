# ============================================
# Production Dockerfile
# Vehicle & Pedestrian Tracking System
# ============================================
# Base: NVIDIA PyTorch image with CUDA support
FROM nvcr.io/nvidia/pytorch:23.08-py3

# Metadata
LABEL maintainer="Vehicle Tracking Project"
LABEL description="Real-time vehicle & pedestrian detection and tracking pipeline"

# Set working directory
WORKDIR /app

# Install system dependencies for OpenCV
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project source code
COPY configs/ configs/
COPY src/ src/
COPY cli.py .

# Create output directories
RUN mkdir -p outputs/videos outputs/logs outputs/metrics models/exported

# Default entrypoint: CLI interface
ENTRYPOINT ["python", "cli.py"]

# Default command (can be overridden)
CMD ["--help"]
