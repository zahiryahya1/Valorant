from ingestion.parser.parser import parse_episode_and_acts
from db.connection import get_connection
from db.insert import insert_episodes, insert_acts
from config.logging import setup_logger
from clients.valorant_api import get_contents

import json

contents = get_contents()

episodes, acts = parse_episode_and_acts(contents)


for ep in episodes:
    print("episodes: " , ep)

for act in acts:
    print("acts: ", act)

conn = get_connection()

insert_episodes(conn, episodes)
insert_acts(conn, acts)
