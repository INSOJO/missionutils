from datetime import datetime, timezone


def validate_lat_lon(lat: float, lon: float) -> bool:
    """Return True if latitude and longitude are valid."""
    return -90 <= lat <= 90 and -180 <= lon <= 180


def normalize_mission_id(text: str) -> str:
    """Clean and normalize a mission ID."""
    return text.strip().lower().replace(" ", "-")


def is_recent_timestamp(ts: str, max_minutes: int = 5) -> bool:
    """
    Return True if the ISO timestamp is within max_minutes of now.
    Expected format example: 2026-03-24T18:30:00+00:00
    """
    dt = datetime.fromisoformat(ts)

    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)

    now = datetime.now(timezone.utc)
    diff_seconds = abs((now - dt).total_seconds())
    return diff_seconds <= max_minutes * 60