"""
ConfigLoader - YAML configuration parser with validation.

Loads and merges configuration files from configs/ directory.
Supports environment variable overrides and CLI argument merging.

Public API:
    class ConfigLoader:
        def __init__(self, config_dir: str = "configs/")
        def load(self, config_name: str) -> dict
        def merge_cli_args(self, config: dict, args: argparse.Namespace) -> dict
"""
