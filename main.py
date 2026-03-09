import json
import logging
from logs.logging_config import setup_logger

from ingestion.pipeline.normalize import normalize_tables
from ingestion.valorant_api import get_user_account_data, get_matches_by_puuid
from ingestion.parser.match_parser import parse_matches

# --- Entry Point for your Main App ---
if __name__ == "__main__":
       
    logger = setup_logger()

    name_input = input("Enter Name: ").strip()
    tag_input = input("Enter Tag: ").strip()

    # Step 1: Get ID/Region
    logger.info("Starting match ingestion pipeline")
    
    puuid, region, e = get_user_account_data(name_input, tag_input)


    if puuid and region:
        
        logger.info(f"Fetched account data - PUUID: {puuid}, Region: {region}")
        
        # Step 2: Get Matches using the ID from Step 1
        raw_matches = get_matches_by_puuid(region, puuid)
        
        # Store raw matches for debugging/inspection. Remove later!
        with open("raw_match.json", "w", encoding="utf-8") as f:
            json.dump(raw_matches, f, ensure_ascii=False, indent=4)
        
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
        with open("parsed_match.json", "w", encoding="utf-8") as f:
            json.dump(parsed_matches, f, ensure_ascii=False, indent=4)
        
    else:
        logger.error(f"Failed to fetch account {name_input}#{tag_input}: {e}")
        exit(1)
                
    tables = normalize_tables(parsed_matches)
    
    # inspecting the normalized tables
    for table_name, records in tables.items():
        logger.info(f"Table: {table_name}, Number of Records: {len(records)}")
        
        
    
    