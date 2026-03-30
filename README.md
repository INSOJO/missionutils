# missionutils

Reusable Python utilities for mission and telemetry data.

## What this project is

`missionutils` is a beginner-friendly Python package built with modern packaging practices.
It includes reusable helper functions for validating telemetry-style inputs such as coordinates,
timestamps, altitude, battery percentage, and mission names.

This project was also built to practice:
- Python packaging with `pyproject.toml`
- automated testing with `pytest`
- CI with GitHub Actions
- dependency vulnerability scanning with `pip-audit`

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
├── pyproject.toml
├── README.md
└── .gitignore
```

## Installation
Clone the repository and install locally:
```bash
git clone https://github.com/YOUR_USERNAME/missionutils.git
cd missionutils
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
```
## Run tests
```bash
PYTHONPATH=src pytest
```
## Build Package
```bash
python -m build
```

## Example usage
```bash
from missionutils.validators import (
    validate_lat_lon,
    validate_battery_pct,
    normalize_mission_id,
)

print(validate_lat_lon(18.4655, -66.1057))   # True
print(validate_battery_pct(87))              # True
print(normalize_mission_id("  Mission Alpha "))  # mission-alpha
```
## Ci and security
This repository uses GitHub Actions to:
- run tests automatically on pushes and pull requests
- build the package
- scan dependencies for known vulnerabilities with pip-audit

## Why I built this?
I built this project to practice real software engineering workflow beyond writing local Python scripts:
packaging, testing, automation, and basic security checks.
