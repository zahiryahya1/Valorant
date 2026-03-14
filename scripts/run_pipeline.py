import json
import logging
from config.logging import setup_logger

from ingestion.transform.normalize import normalize_tables
from clients.valorant_api import get_user_account_data, get_matches_by_puuid, get_stored_matches, get_match_by_id
from ingestion.parser.parser import parse_matches, parse_stored_matches
from db.insert import *
from db.fetch import get_current_season
from db.connection import get_connection

# --- Entry Point for your Main App ---
if __name__ == "__main__":
       
    logger = setup_logger()

    name_input = input("Enter Name: ").strip()
    tag_input = input("Enter Tag: ").strip()
    # mode = input("Enter Game Mode (Competative vs All): ").strip()

    # Step 1: Get ID/Region
    logger.info("Starting match ingestion pipeline")
    conn = get_connection()

    
    puuid, region, e = get_user_account_data(name_input, tag_input)


    if puuid and region:
        
        logger.info(f"Fetched account data - PUUID: {puuid}, Region: {region}. Now fetching Matches")
        
        # Step 2: Get Matches using the ID from Step 1
        stored_matches = get_stored_matches(region, puuid)
        
        if stored_matches is None:
            exit(1)
        
        # Step 3: Get season or previous season

        season_id = get_current_season(conn)
        
        match_ids = parse_stored_matches(season_id, stored_matches)
        
        if match_ids is None:
            logger.info("Failed to fetch this seasons matches. Exiting.")
            exit(1)
        
        
        try:
            # step 4: get match data & parse them
            raw_matches = []
            for id in match_ids:
                raw_matches.append(get_match_by_id(id))
            

            parsed_matches = parse_matches(raw_matches)
            
            logger.info(f"Parsed {len(parsed_matches)} matches")
            
        except Exception as e:
            logger.error(f"Error occurred while parsing matches: {e}")
            exit(1)

        # step 4: Store Parsed Data
        with open("./data/processed/parsed_season_matches.json", "w", encoding="utf-8") as f:
            json.dump(parsed_matches, f, ensure_ascii=False, indent=4, default=str)
        
    else:
        logger.error(f"Failed to fetch account {name_input}#{tag_input}: {e}")
        exit(1)
                
    tables = normalize_tables(parsed_matches)
    
    
    # inspecting the normalized tables
    for table_name, records in tables.items():
        logger.info(f"Table: {table_name}, Number of Records: {len(records)}")
        
    
    insert_players(conn, tables["players"])

    insert_matches(conn, tables["matches"])

    insert_player_match_stats(conn, tables["player_match_stats"])

    insert_rounds(conn, tables["rounds"])

    insert_damage_events(conn, tables["damage_events"])

    insert_kill_events(conn, tables["kill_events"])
    