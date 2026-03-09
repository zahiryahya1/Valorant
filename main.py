import json
import logging
from logs.logging_config import *

from ingestion.pipeline.normalize import normalize_tables
from ingestion.valorant_api import get_user_account_data, get_matches_by_puuid
from ingestion.parser.match_parser import parse_matches

# --- Entry Point for your Main App ---
if __name__ == "__main__":
       

    name_input = input("Enter Name: ").strip()
    tag_input = input("Enter Tag: ").strip()

    # Step 1: Get ID/Region
    logging.info("Starting match ingestion pipeline")
    
    try:
        puuid, region = get_user_account_data(name_input, tag_input)
        logging.info("Fetched account data successfully")
    except Exception as e:
        logging.error(f"Error occurred while fetching user account data: {e}. Account may not not be public or may not exist.")
        exit(1)

    if puuid and region:
        # Step 2: Get Matches using the ID from Step 1
        raw_matches = get_matches_by_puuid(region, puuid)
        
        # Store raw matches for debugging/inspection. Remove later!
        with open("raw_match.json", "w", encoding="utf-8") as f:
            json.dump(raw_matches, f, ensure_ascii=False, indent=4)
        
        if raw_matches is None:
            print("Failed to fetch matches. Exiting.")
            exit(1)
        
        # step 3: Parse Matches
        try:
            parsed_matches = parse_matches(raw_matches)
            logging.info(f"Parsed {len(parsed_matches)} matches")
        except Exception as e:
            logging.error(f"Error occurred while parsing matches: {e}")
            exit(1)

        # step 4: Store Parsed Data
        with open("parsed_match.json", "w", encoding="utf-8") as f:
            json.dump(parsed_matches, f, ensure_ascii=False, indent=4)
        
    else:
        print("Could not proceed without valid user data.")
                
    tables = normalize_tables(parsed_matches)
    
    # inspecting the normalized tables
    for table_name, records in tables.items():
        logging.info(f"Table: {table_name}, Number of Records: {len(records)}")
        
        
    
    