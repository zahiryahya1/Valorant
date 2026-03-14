from ingestion.parser.parser import parse_stored_data
from clients.valorant_api import get_match_by_id

import json

test_puuid = "f9f26d15-776c-57a0-b6bf-be1fc1d3c443"

with open("./data/raw/test_stored_matches.json", "r") as f:
    stored_matches = json.load(f)

match_ids = parse_stored_data(stored_matches["data"])

matches = []


# because I am fetching a bunch of match data, I will need to have a wait time. 
for id in match_ids:
    print(id)
    matches.append(get_match_by_id(id))
    
print(matches)
exit()

with open("./data/processed/test_parsed_stored_matches.json", "w", encoding="utf-8") as f:
    json.dump(match_ids, f, ensure_ascii=False, indent=4, default=str)
    


