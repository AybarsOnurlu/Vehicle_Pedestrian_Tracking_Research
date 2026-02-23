"""
Setup script for vehicle_pedestrian_tracking package.

Allows the project to be installed as a Python package:
    pip install -e .
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

with open("requirements.txt", "r", encoding="utf-8") as f:
    requirements = [
        line.strip() for line in f if line.strip() and not line.startswith("#")
    ]

setup(
    name="vehicle-pedestrian-tracking",
    version="0.1.0",
    author="Vehicle Tracking Research Team",
    description="Real-time vehicle & pedestrian detection and multi-object tracking system",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/<username>/vehicle-pedestrian-tracking",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.9",
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "vpt-track=cli:main",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
)
