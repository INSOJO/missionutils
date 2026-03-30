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

def validate_altitude_m(altitude_m: float) -> bool:
    """Return True if altitude is in a reasonable telemetry range."""
    return -500 <= altitude_m <= 50000


def validate_battery_pct(battery_pct: float) -> bool:
    """Return True if battery percentage is between 0 and 100."""
    return 0 <= battery_pct <= 100


def is_nonempty_mission_name(text: str) -> bool:
    """Return True if mission name has at least one non-space character."""
    return bool(text and text.strip())


def validate_temperature_c(temp_c: float) -> bool:
    """Return True if temperature is in a reasonable environmental range."""
    return -100 <= temp_c <= 100