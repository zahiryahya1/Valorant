# ==========================================================
# SAFE JSON ACCESS HELPER
# ==========================================================

from datetime import datetime

# - Safe parsing (handles null and missing keys)
def safe_get(data, *keys, default=None):

    current = data

    for key in keys:

        if current is None:
            return default

        if isinstance(current, dict):
            current = current.get(key)

        elif isinstance(current, list) and isinstance(key, int):

            if key < len(current):
                current = current[key]
            else:
                return default

        else:
            return default

    return current if current is not None else default


def parse_game_date(date_str):
    return datetime.strptime(date_str, "%A, %B %d, %Y %I:%M %p")