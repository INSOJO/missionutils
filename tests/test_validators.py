from datetime import datetime, timezone, timedelta

from missionutils.validators import (
    validate_lat_lon,
    normalize_mission_id,
    is_recent_timestamp,
)


def test_validate_lat_lon_valid():
    assert validate_lat_lon(18.4655, -66.1057) is True


def test_validate_lat_lon_invalid():
    assert validate_lat_lon(100, -66.1057) is False


def test_normalize_mission_id():
    assert normalize_mission_id("  Mission Alpha  ") == "mission-alpha"


def test_recent_timestamp_true():
    recent = datetime.now(timezone.utc) - timedelta(minutes=2)
    assert is_recent_timestamp(recent.isoformat(), max_minutes=5) is True


def test_recent_timestamp_false():
    old = datetime.now(timezone.utc) - timedelta(minutes=10)
    assert is_recent_timestamp(old.isoformat(), max_minutes=5) is False