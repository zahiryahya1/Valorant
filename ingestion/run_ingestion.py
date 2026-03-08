import json

from valorant_api import get_user_account_data, get_matches_by_puuid
from parser import parse_matches

# --- Entry Point for your Main App ---
if __name__ == "__main__":
       

    name_input = input("Enter Name: ").strip()
    tag_input = input("Enter Tag: ").strip()

    # Step 1: Get ID/Region
    puuid, region = get_user_account_data(name_input, tag_input)

    if puuid and region:
        # Step 2: Get Matches using the ID from Step 1
        print(f"Found PUUID: {puuid}. Fetching matches...")
        matches = get_matches_by_puuid(region, puuid)
        
        with open("raw_match.json", "w", encoding="utf-8") as f:
            json.dump(matches, f, ensure_ascii=False, indent=4)
        
        if matches is None:
            print("Failed to fetch matches. Exiting.")
            exit(1)
        
        # step 3: Parse Matches
        parsed_matches = parse_matches(matches)
        
        # step 4: Store Parsed Data
        with open("parsed_match.json", "w", encoding="utf-8") as f:
            json.dump(parsed_matches, f, ensure_ascii=False, indent=4)
        
    else:
        print("Could not proceed without valid user data.")
        

    
    