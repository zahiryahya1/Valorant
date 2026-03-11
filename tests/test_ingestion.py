from ingestion.parser.match_parser import parse_matches

import json

test_puuid = "f9f26d15-776c-57a0-b6bf-be1fc1d3c443"

with open("./data/raw/test_matches.json", "r") as f:
    matches_data = json.load(f)

# each game in the list of matches is a dictionary with keys "metadata", "players", and "rounds".

parsed_matches = parse_matches(matches_data["data"])

with open("./data/processed/test_parsed_matches.json", "w", encoding="utf-8") as f:
    json.dump(parsed_matches, f, ensure_ascii=False, indent=4, default=str)
    


