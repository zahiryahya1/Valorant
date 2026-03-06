import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Constants
API_KEY = os.getenv("HENRIKDEV_API_KEY")
BASE_URL = "https://api.henrikdev.xyz/valorant"

def get_session():
    """Creates a pre-configured session for API calls."""
    session = requests.Session()
    session.headers.update({"Authorization": API_KEY})
    return session

def get_user_account_data(name: str, tag: str):
    """
    Given a name and tag, returns a tuple of (puuid, region).
    Returns (None, None) if the user is not found.
    """
    session = get_session()
    url = f"{BASE_URL}/v2/account/{name}/{tag}"
    
    try:
        response = session.get(url)
        response.raise_for_status()
        data = response.json().get("data", {})
        
        return data.get("puuid"), data.get("region")
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching account for {name}#{tag}: {e}")
        return None, None

def get_matches_by_puuid(region: str, puuid: str):
    """
    Given a region and puuid, returns the match history JSON.
    """
    if not region or not puuid:
        return None

    session = get_session()
    url = f"{BASE_URL}/v3/by-puuid/matches/{region}/{puuid}"
    
    try:
        response = session.get(url)
        response.raise_for_status()
        return response.json()
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching matches for {puuid}: {e}")
        return None

