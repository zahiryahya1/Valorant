# Helper functions for data ingestion and API interaction

import json
from typing import Any

def dump_to_json(data: Any, filename: str):
    """Dump data to a pretty-printed JSON file."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)