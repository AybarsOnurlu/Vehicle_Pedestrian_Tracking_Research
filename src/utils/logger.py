"""
Logger - Structured logging with stderr routing.

Following CLI best practices:
    - stdout: Reserved for machine-readable JSON telemetry
    - stderr: All system logs, warnings, errors, and debug info

Public API:
    def get_logger(name: str, level: str = "INFO") -> logging.Logger
"""
