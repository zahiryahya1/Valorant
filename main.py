import json

from ingestion.pipeline.normalize import normalize_tables
from ingestion.valorant_api import get_user_account_data, get_matches_by_puuid
from ingestion.parser.match_parser import parse_matches

# --- Entry Point for your Main App ---
if __name__ == "__main__":
       

    name_input = input("Enter Name: ").strip()
    tag_input = input("Enter Tag: ").strip()

    # Step 1: Get ID/Region
    puuid, region = get_user_account_data(name_input, tag_input)

    if puuid and region:
        # Step 2: Get Matches using the ID from Step 1
        print(f"Found PUUID: {puuid}. Fetching matches...")
        raw_matches = get_matches_by_puuid(region, puuid)
        
        with open("raw_match.json", "w", encoding="utf-8") as f:
            json.dump(raw_matches, f, ensure_ascii=False, indent=4)
        
        if raw_matches is None:
            print("Failed to fetch matches. Exiting.")
            exit(1)
        
        # step 3: Parse Matches
        parsed_matches = parse_matches(raw_matches)
        
        # step 4: Store Parsed Data
        with open("parsed_match.json", "w", encoding="utf-8") as f:
            json.dump(parsed_matches, f, ensure_ascii=False, indent=4)
        
    else:
        print("Could not proceed without valid user data.")
                
    tables = normalize_tables(parsed_matches)
    
    # inspecting the normalized tables
    for table_name, records in tables.items():
        print(f"Table: {table_name}, Number of Records: {len(records)}")
        
        
    
    