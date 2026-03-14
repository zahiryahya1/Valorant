import json
import logging
from config.logging import setup_logger

from ingestion.transform.normalize import normalize_tables
from clients.valorant_api import get_user_account_data, get_matches_by_puuid
from ingestion.parser.parser import parse_matches
from db.insert import *
from db.connection import get_connection

# --- Entry Point for your Main App ---
if __name__ == "__main__":
       
    logger = setup_logger()

    name_input = input("Enter Name: ").strip()
    tag_input = input("Enter Tag: ").strip()
    # mode = input("Enter Game Mode (Competative vs All): ").strip()

    # Step 1: Get ID/Region
    logger.info("Starting match ingestion pipeline")
    
    puuid, region, e = get_user_account_data(name_input, tag_input)


    if puuid and region:
        
        logger.info(f"Fetched account data - PUUID: {puuid}, Region: {region}.\nNow fetching Matches")
        
        # Step 2: Get Matches using the ID from Step 1
        raw_matches = get_matches_by_puuid(region, puuid)
        
        if raw_matches is None:
            logger.info("Failed to fetch matches. Exiting.")
            exit(1)
        
        # step 3: Parse Matches
        try:
            parsed_matches = parse_matches(raw_matches)
            logger.info(f"Parsed {len(parsed_matches)} matches")
        except Exception as e:
            logger.error(f"Error occurred while parsing matches: {e}")
            exit(1)

        # step 4: Store Parsed Data
        with open("./data/processed/parsed_matches.json", "w", encoding="utf-8") as f:
            json.dump(parsed_matches, f, ensure_ascii=False, indent=4, default=str)
        
    else:
        logger.error(f"Failed to fetch account {name_input}#{tag_input}: {e}")
        exit(1)
                
    tables = normalize_tables(parsed_matches)
    
    
    # inspecting the normalized tables
    for table_name, records in tables.items():
        logger.info(f"Table: {table_name}, Number of Records: {len(records)}")
        
    conn = get_connection()

    
    insert_players(conn, tables["players"])

    insert_matches(conn, tables["matches"])

    insert_player_match_stats(conn, tables["player_match_stats"])

    insert_rounds(conn, tables["rounds"])

    insert_damage_events(conn, tables["damage_events"])

    insert_kill_events(conn, tables["kill_events"])
    