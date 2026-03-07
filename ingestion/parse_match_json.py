# for each match in match json, extract relevant data.


def parse_matches(matches, puuid):
    
    parsed_matches = []
    
    for match in matches:
        
        metadata = match.get("metadata")
        parsed_metatdata = parse_metadata(metadata)
        match_id = parsed_metatdata.get("match_id")

        # determine which team has won to update player stats accordingly.
        red_has_won = match.get("teams").get("red").get("has_won")    
        
        players = match.get("players").get("all_players")
        
        stats = parse_match_player_stats(players, puuid, match_id, red_has_won)
        
        rounds = match.get("rounds")
        parsed_rounds = parse_rounds(rounds, puuid, match_id)
        
        parsed_damage_events = parse_damage_events(rounds, puuid, match_id)
        
        parsed_kill_events = parse_kill_events(match, puuid, match_id)
        
        parsed_match = {
            "metadata": parsed_metatdata,
            "player_stats": stats,
            "rounds": parsed_rounds,
            "damage_events": parsed_damage_events,
            "kill_events": parsed_kill_events
        }
        
        parsed_matches.append(parsed_match)
    
    return parsed_matches



def parse_metadata(metadata): 
    
    parsed = {
        "match_id": metadata.get("matchid"),
        "map": metadata.get("map"),
        "game_mode": metadata.get("mode"),
        "date_played": metadata.get("game_start_patched"),
        "game_start": metadata.get("game_start"),
        "game_length_sec": metadata.get("game_length"),
        "rounds_played": metadata.get("rounds_played"),
        "season_id": metadata.get("season_id"),
        "version": metadata.get("game_version"),
    }
    
    return parsed
    
    
def parse_match_player_stats(players, test_puuid, match_id, red_has_won): 
    
    # get the stats for the player with the given puuid.
    for player in players:
        if player.get("puuid") == test_puuid:
            player_stats = player
            break
    
    # determine if the player won or lost the match based on the team they were on and which team won.
    won = False
    if red_has_won and player_stats["team"].lower() == "red":
        won = True
    
    stats = player_stats.get("stats")
    # create a dictionary of the relevant player stats to be inserted into the database.
    player_stats = {
        "player_puuid": player_stats.get("puuid"),
        "match_id": match_id,
        "team": player_stats.get("team"),
        "agent": player_stats.get("character"),
        "rank": player_stats.get("currenttier_patched"),
        "won": won,
        
        "kills": stats.get("kills"),
        "deaths": stats.get("deaths"),
        "assists": stats.get("assists"),
        "score": stats.get("score"),
        "damage": player_stats.get("damage_made"),
        
        "bodyshots": stats.get("bodyshots"),
        "legshots": stats.get("legshots"),
        "headshots": stats.get("headshots"),
        
        "afk_rounds": player_stats.get("behavior").get("afk_rounds"),
        "friendly_fire_incoming": player_stats.get("behavior").get("friendly_fire").get("incoming"),
        "friendly_fire_outgoing": player_stats.get("behavior").get("friendly_fire").get("outgoing"),
    }
    
    return player_stats

def parse_rounds(rounds, puuid, match_id):
    
    parsed_rounds = []
    round_num = 1
    for round in rounds:
        
        planted_by = round.get("plant_events").get("planted_by", {})
        defunseed_by = round.get("defuse_events").get("defused_by", {})
        parsed_round = {
            "match_id": match_id,
            "round_num": round_num,
            "winning_team": round.get("winning_team").lower(),
            "bomb_planted_player": planted_by.get("puuid"),    # I jsut want puuid but i get the player info as a set 
            "bomb_defused_player": defunseed_by.get("puuid"),
            "round_end_reason": round.get("end_type")
        }
        
        parsed_rounds.append(parsed_round)
        round_num += 1
    
    return parsed_rounds

def parse_damage_events(rounds, puuid, match_id):
    
    parsed_dmg_events = []
    round_num = 1
    for round in rounds:
        for player_stats in round.get("player_stats"):
            if player_stats.get("player_puuid") == puuid:
                # we can also extract player-specific events here if needed.
                
                damage_events = player_stats.get("damage_events")
                
                for dmg_event in damage_events:
                    
                    data = {
                        "match_id": match_id,
                        "round_num": round.get("round_num"),
                        "killer_puuid": dmg_event.get("killer_puuid"),
                        "victim_puuid": dmg_event.get("victim_puuid"),
                        "damage": dmg_event.get("damage"),
                        "damage_type": dmg_event.get("damage_type"),
                        "is_headshot": dmg_event.get("is_headshot")
                    }
                    
                    parsed_dmg_events.append(data)
                    break # break here since we only want damage events where the player is the receiver.
                
        round_num += 1
                        
                        
    # calculate damage recieved by iterating through all player stats and searching for receiver_puuid = puuid in the damage events. we can also calculate friendly fire damage taken by filtering for events where the killer and receiver are on the same team.
    round_num = 1
    for round in rounds:
        for player_stats in round.get("player_stats"):
            damage_events = player_stats.get("damage_events")
            for dmg_event in damage_events:
                if dmg_event.get("receiver_puuid") == puuid:
                    data = {
                        "match_id": match_id,
                        "round_num": round.get("round_num"),
                        "attacker_puuid": dmg_event.get("attacker_puuid"),
                        "receiver_puuid": dmg_event.get("receiver_puuid"),
                        "damage": dmg_event.get("damage"),
                        "headshot": dmg_event.get("headshot"),
                        "bodyshot": dmg_event.get("bodyshot"),
                        "headshot": dmg_event.get("headshot")
                    }
                    parsed_dmg_events.append(data)
        round_num += 1
    return parsed_dmg_events


def parse_kill_events(match, puuid, match_id):
    
    parsed_kill_events = []

    kill_events = match.get("kills")
    
    for kill in kill_events:
        if kill.get("killer_puuid") == puuid or kill.get("victim_puuid") == puuid:
            data = {
                "match_id": match_id,
                "round_num": kill.get("round"),
                "kill_time_in_round": kill.get("kill_time_in_round"),
                "killer_puuid": kill.get("killer_puuid"),
                "victim_puuid": kill.get("victim_puuid"),
                "killer_team": kill.get("killer_team").lower(),
                "victim_team": kill.get("victim_team").lower(),
                "weapon": kill.get("damage_weapon_name"),
            }
            parsed_kill_events.append(data)
    