from datetime import datetime, timezone, timedelta

from missionutils.validators import (
    validate_lat_lon,
    normalize_mission_id,
    is_recent_timestamp,
    validate_altitude_m,
    validate_battery_pct,
    is_nonempty_mission_name,
    validate_temperature_c,
)
from missionutils.utils import safe_float


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


def test_validate_altitude_valid():
    assert validate_altitude_m(1200) is True


def test_validate_altitude_invalid():
    assert validate_altitude_m(100000) is False


def test_validate_battery_valid():
    assert validate_battery_pct(75) is True


def test_validate_battery_invalid():
    assert validate_battery_pct(120) is False


def test_nonempty_mission_name_valid():
    assert is_nonempty_mission_name("STRATOS Mission 1") is True


def test_nonempty_mission_name_invalid():
    assert is_nonempty_mission_name("   ") is False


def test_validate_temperature_valid():
    assert validate_temperature_c(24.5) is True


def test_validate_temperature_invalid():
    assert validate_temperature_c(180) is False


def test_safe_float_valid_string():
    assert safe_float("3.14") == 3.14


def test_safe_float_invalid_string():
    assert safe_float("abc") is None


def test_safe_float_invalid_string_with_default():
    assert safe_float("abc", default=0.0) == 0.0