import logging
import os
import requests
from dotenv import load_dotenv
from typing import Optional, Tuple, Dict, Any

# -----------------------------
# Load environment variables
# -----------------------------
load_dotenv()
API_KEY = os.getenv("HENRIKDEV_API_KEY")
BASE_URL = "https://api.henrikdev.xyz/valorant"

# -----------------------------
# Session management
# -----------------------------
_session: Optional[requests.Session] = None

def get_session() -> requests.Session:
    """Return a session with the API key set (singleton)."""
    global _session
    if _session is None:
        _session = requests.Session()
        _session.headers.update({"Authorization": API_KEY})
    return _session

# -----------------------------
# API functions
# -----------------------------
def get_user_account_data(name: str, tag: str) -> Tuple[Optional[str], Optional[str], Optional[Exception]]:
    """Fetches PUUID and region for a Valorant account."""
    session = get_session()
    url = f"{BASE_URL}/v2/account/{name}/{tag}"
    try:
        response = session.get(url)
        response.raise_for_status()
        data = response.json().get("data", {})
        return data.get("puuid"), data.get("region"), None
    except requests.exceptions.RequestException as e:
        return None, None, e

def get_matches_by_puuid(region: str, puuid: str) -> Optional[Dict[str, Any]]:
    """Fetches match history for a given region and PUUID."""
    if not region or not puuid:
        print("[WARN] Region or PUUID not provided")
        return None
    session = get_session()
    url = f"{BASE_URL}/v3/by-puuid/matches/{region}/{puuid}"
    try:
        response = session.get(url)
        response.raise_for_status()
        
        matches = response.json().get("data", {})
        
        if not matches:
            print(f"[INFO] No matches found for PUUID {puuid} in region {region}")
            return None
        return matches
    
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Failed to fetch matches for PUUID {puuid}: {e}")
        return None