"""
Pipeline Module
===============

Orchestrates the end-to-end execution flow from video input to tracked output.

Key Components:
    - PipelineRunner: Main execution loop connecting all stages
    - StageRegistry: Dynamic stage loading from configuration

The pipeline follows a strict sequential flow:
    Ingest → Preprocess → Detect → Post-Process → Track → Output
"""
