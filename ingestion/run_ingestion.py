from fetch_matches import get_user_account_data, get_matches_by_puuid

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
        
        if matches:
            count = len(matches.get('data', []))
            print(f"Successfully retrieved {count} matches.")
    else:
        print("Could not proceed without valid user data.")
        
    print("Ingestion process completed.")
    