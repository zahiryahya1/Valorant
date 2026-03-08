# ==========================================================
# SAFE JSON ACCESS HELPER
# ==========================================================

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