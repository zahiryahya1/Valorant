def normalize_tables(parsed_matches):

    tables = {
        "matches": [],
        "players": [],
        "player_match_stats": [],
        "rounds": [],
        "damage_events": [],
        "kill_events": []
    }

    for match in parsed_matches:

        tables["matches"].append(match["metadata"])

        tables["players"].extend(match["players_info"])

        tables["player_match_stats"].extend(match["players_stats"])

        tables["rounds"].extend(match["rounds"])

        tables["damage_events"].extend(match["damage_events"])
        
        tables["kill_events"].extend(match["kill_events"])


    # Deduplicate players
    unique_players = {}

    for player in tables["players"]:
        unique_players[player["player_puuid"]] = player

    tables["players"] = list(unique_players.values())

    return tables