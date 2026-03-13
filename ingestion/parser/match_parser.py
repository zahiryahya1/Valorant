# ==========================================================
# Valorant Match Parser
# ==========================================================
# Parses Riot API match JSON into normalized tables.
#
# Design Goals:
# - Safe parsing (handles null and missing keys)
# - Single-pass round parsing
# - Event extractor pattern for scalability
# - Clean architecture for analytics pipelines
# ==========================================================

from .helpers import safe_get
from datetime import datetime

# ==========================================================
# MAIN MATCH PARSER
# ==========================================================

# requirements - Dict of matches 
# returns a list of parsed matches

def parse_matches(matches):

    parsed_matches = []

    for match in matches:

        metadata = parse_metadata(safe_get(match, "metadata", default={}))

        context = {
            "match_id": metadata["match_id"],
            "red_has_won": safe_get(match, "teams", "red", "has_won")
        }
        

        players = safe_get(match, "players", "all_players", default=[])

        player_match_stats = parse_player_info_and_stats(players, context)

        rounds = safe_get(match, "rounds", default=[])

        round_data = parse_rounds(rounds, context)

        kill_events = extract_kill_events(match, context)

        parsed_matches.append({

            "metadata": metadata,
            "players_info": player_match_stats.get("players_info", []),
            "players_stats": player_match_stats.get("players_stats", []),

            "rounds": round_data["rounds"],
            "damage_events": round_data["damage_events"],

            "kill_events": kill_events
        })

    return parsed_matches


# ==========================================================
# METADATA PARSER
# ==========================================================

def parse_metadata(metadata):

    date_str = safe_get(metadata, "game_start_patched")
    date_played = datetime.strptime(
    date_str,
    "%A, %B %d, %Y %I:%M %p"
    )
    
    game_start = datetime.fromtimestamp(safe_get(metadata, "game_start"))
    

    return {

        "match_id": safe_get(metadata, "matchid"),
        "map": safe_get(metadata, "map"),
        "game_mode": safe_get(metadata, "mode"),

        "date_played": date_played,
        "game_start": game_start,

        "game_length_sec": int(safe_get(metadata, "game_length", default=0)),
        "rounds_played": int(safe_get(metadata, "rounds_played", default=0)),

        "season_id": safe_get(metadata, "season_id"),
        
        # need to get season and act names by calling valorant api
        "season_name": None,
        "act_id": None,
        "act_name": None,
        
        "version": safe_get(metadata, "game_version"),
    }


# ==========================================================
# PLAYER STATS PARSER
# ==========================================================

def extract_match_stats(players, context):

    parsed_players = []

    red_has_won = context.get("red_has_won")
    match_id = context.get("match_id")

    for player in players:

        team = (safe_get(player, "team", default="") or "").lower()

        # Determine if the player's team won or lost based on the "red_has_won" 
        # flag and the player's team
        won = (
            (team == "red" and red_has_won) or
            (team == "blue" and not red_has_won)
        )

        stats = safe_get(player, "stats", default={})

        parsed_players.append({

            "puuid": safe_get(player, "puuid"),
            "match_id": match_id,

            "team": team,
            "agent": safe_get(player, "character").lower(),
            "rank": safe_get(player, "currenttier_patched"),

            "won": won,

            "kills": int(safe_get(stats, "kills", default=0)),
            "deaths": int(safe_get(stats, "deaths", default=0)),
            "assists": int(safe_get(stats, "assists", default=0)),

            "score": int(safe_get(stats, "score", default=0)),

            "damage": int(safe_get(player, "damage_made", default=0)),

            "headshots": int(safe_get(stats, "headshots", default=0)),
            "bodyshots": int(safe_get(stats, "bodyshots", default=0)),
            "legshots": int(safe_get(stats, "legshots", default=0)),

            "afk_rounds": int(safe_get(player, "behavior", "afk_rounds", default=0)),
            "friendly_fire_incoming": int(safe_get(player, "behavior", "friendly_fire", "incoming", default=0)),
            "friendly_fire_outgoing": int(safe_get(player, "behavior", "friendly_fire", "outgoing", default=0)),
        })

    return parsed_players


# =========================================================
# Player Info and Stats Parser
# =========================================================

def parse_player_info_and_stats(players, context):
    players_info = []

    red_has_won = context.get("red_has_won")
    match_id = context.get("match_id")

    for player in players:
        player_info = extract_player_info(player)
        players_info.append(player_info)

    parsed_player_match_stats = extract_match_stats(players, context)

    return {
        "players_info": players_info,
        "players_stats": parsed_player_match_stats,
    }
    
    
# ==========================================================
# Player Info Extractor
# ==========================================================
def extract_player_info(player):

    return {

        "puuid": safe_get(player, "puuid"),
        "game_name": safe_get(player, "name"),
        "tag": safe_get(player, "tag"),
    }



# ==========================================================
# ROUND PARSER (Single Pass)
# ==========================================================

def parse_rounds(rounds, context):

    rounds_table = []
    damage_events = []
    match_id = context.get("match_id")

    for round_number, round_data in enumerate(rounds, start=1):

        rounds_table.append(
            extract_round_summary(round_data, match_id, round_number)
        )

        
        damage_events.extend(
            extract_damage_events(round_data, match_id, round_number)
        )

    return {

        "rounds": rounds_table,
        "damage_events": damage_events,
    }


# ==========================================================
# EVENT EXTRACTORS
# ==========================================================


def extract_round_summary(round_data, match_id, round_number):

    return {

        "match_id": match_id,
        "round_number": int(round_number),

        "winning_team": (safe_get(round_data, "winning_team", default="") or "").lower(),

        "round_end_reason": safe_get(round_data, "end_type"),
        
        "bomb_planted_player": safe_get(round_data, "plant_events", "planted_by", "puuid"),
        "bomb_defused_player": safe_get(round_data, "defuse_events", "defused_by", "puuid")
    }



def extract_damage_events(round_data, match_id, round_number):
    
    events = []

    player_match_stats = safe_get(round_data, "player_stats", default=[])
    for player in player_match_stats:

        damage_events = safe_get(player, "damage_events", default=[])
        
        attacker = safe_get(player, "player_puuid")
        
        for dmg in damage_events:

            receiver = safe_get(dmg, "receiver_puuid")

            events.append({

                "match_id": match_id,
                "round_number": int(round_number),

                "attacker_puuid": attacker,
                "receiver_puuid": receiver,

                "damage": int(safe_get(dmg, "damage", default=0)),
                "headshots": int(safe_get(dmg, "headshots", default=0)),
                "bodyshots": int(safe_get(dmg, "bodyshots", default=0)),
                "legshots": int(safe_get(dmg, "legshots", default=0)),
            })
        
    return events


# ==========================================================
# KILL EVENT PARSER
# ==========================================================

def extract_kill_events(match, context):

    kill_events = safe_get(match, "kills", default=[])
    match_id = context.get("match_id")

    parsed = []


    for kill in kill_events:

        parsed.append({

            "match_id": match_id,

            "round_number": int(safe_get(kill, "round", default=0)),

            "kill_time_in_round": int(safe_get(kill, "kill_time_in_round", default=0)),

            "killer_puuid": safe_get(kill, "killer_puuid"),
            "victim_puuid": safe_get(kill, "victim_puuid"),

            "killer_team": (safe_get(kill, "killer_team", default="") or "").lower(),
            "victim_team": (safe_get(kill, "victim_team", default="") or "").lower(),

            "weapon": safe_get(kill, "damage_weapon_name")
        })

    return parsed


# ==========================================================
# EXTRACTS MATCH HISTORY GAME ID'S
# ==========================================================

def parse_stored_data(data):
    
    match_ids = []
    
    for match in data:
        match_id = safe_get(match, "meta", "id", default={})
        
        match_ids.append(match_id)


    return match_ids


