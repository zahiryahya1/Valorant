from ingestion.parser.match_parser import parse_matches
from db.connection import get_connection
from ingestion.transform.normalize import normalize_tables
from db.insert import insert_players
from config.logging import setup_logger

import json

test_puuid = "f9f26d15-776c-57a0-b6bf-be1fc1d3c443"
logger = setup_logger()

with open("./data/raw/test_matches.json", "r") as f:
    matches_data = json.load(f)

# each game in the list of matches is a dictionary with keys "metadata", "players", and "rounds".

conn = get_connection()

parsed_matches = parse_matches(matches_data["data"])

tables = normalize_tables(parsed_matches)

insert_players(conn, tables["players"])
