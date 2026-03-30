def safe_float(value, default=None):
    """
    Try to convert value to float.
    Return default if conversion fails.
    """
    try:
        return float(value)
    except (TypeError, ValueError):
        return default