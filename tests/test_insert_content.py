from ingestion.parser.parser import parse_episode_and_acts
from db.connection import get_connection
from db.insert import insert_episodes, insert_acts
from config.logging import setup_logger
from clients.valorant_api import get_contents
from db.fetch import get_current_season, get_previous_season

import json

contents = get_contents()

episodes, acts = parse_episode_and_acts(contents)

conn = get_connection()

season_id = get_current_season(conn)

previous_id = get_previous_season(conn)

print("current season: ", season_id)
print("previous season: ", previous_id)

# insert_episodes(conn, episodes)
# insert_acts(conn, acts)
