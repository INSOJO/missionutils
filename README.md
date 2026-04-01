# missionutils
![CI](https://github.com/INSOJO/missionutils/actions/workflows/ci.yml/badge.svg)

Reusable Python utilities for mission and telemetry data.

## Overview
`missionutils` is a lightweight Python utility library for validating telemetry-style data commonly used in mission and sensor systems.
It provides reusable helper functions for:
- geographic coordinate validation
- telemetry timestamp freshness checks
- altitude and battery sanity checks
- mission identifier normalization
- safe numeric conversions

This project was built to practice modern Python engineering workflows, including:
- Python packaging using pyproject.toml
- automated testing with pytest
- CI pipelines with GitHub Actions dependency vulnerability scanning with pip-audit

## Features

- Validate latitude and longitude
- Normalize mission IDs
- Check timestamp freshness
- Validate altitude range
- Validate battery percentage
- Validate temperature range
- Safely convert values to float

## Project structure

```text
missionutils/
├── src/
│   └── missionutils/
│       ├── __init__.py
│       ├── validators.py
│       └── utils.py
├── tests/
│   └── test_validators.py
├── .github/
│   └── workflows/
│       └── ci.yml
│       └── publish-testpypi.yml
├── pyproject.toml
├── README.md
└── .gitignore
```

## Installation
### Local Development
Clone the repository and install locally:
```bash
git clone https://github.com/YOUR_USERNAME/missionutils.git
cd missionutils
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
```
### Future package installation
Once published, the package could be installed with:
```bash
pip install missionutils
```
## Example usage
```python
from missionutils.validators import (
    validate_lat_lon,
    validate_battery_pct,
    normalize_mission_id,
)

print(validate_lat_lon(18.4655, -66.1057))   # True
print(validate_battery_pct(87))              # True
print(normalize_mission_id("  Mission Alpha "))  # mission-alpha
```
## Run tests
```bash
PYTHONPATH=src pytest
```
## Build Package
```bash
python -m build
```

## CI and security
This repository uses GitHub Actions to:
- run tests automatically on pushes and pull requests
- build the package
- scan dependencies for known vulnerabilities with pip-audit

## CI and Security
This repository includes a GitHub Actions workflow that automatically:
- runs unit tests on every push and pull request
- builds the Python package
- scans dependencies for known vulnerabilities using pip-audit

This ensures code quality and dependency security before releases.

## Why This Project Exists
This project was created to practice real software engineering workflows beyond simple scripts, including:
- Building reusable Python libraries
- Structuring packages using modern Python packaging standards
- Automating testing and builds with CI pipelines
- Performing basic dependency security checks.
