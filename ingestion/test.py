from parser import parse_matches

import json

test_puuid = "f9f26d15-776c-57a0-b6bf-be1fc1d3c443"

with open("../data/test/matches.json", "r") as f:
    matches_data = json.load(f)

# each game in the list of matches is a dictionary with keys "metadata", "players", and "rounds".
matches = matches_data.get("data")

parsed_matches = parse_matches(matches, test_puuid)

with open("match1.json", "w", encoding="utf-8") as f:
    json.dump(parsed_matches, f, ensure_ascii=False, indent=4)