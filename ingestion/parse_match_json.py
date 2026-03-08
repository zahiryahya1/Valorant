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


# ==========================================================
# SAFE JSON ACCESS HELPER
# ==========================================================

def safe_get(data, *keys, default=None):

    current = data

    for key in keys:

        if current is None:
            return default

        # dictionary access
        if isinstance(current, dict):
            current = current.get(key)

        # list access
        elif isinstance(current, list) and isinstance(key, int):

            if key < len(current):
                current = current[key]
            else:
                return default

        else:
            return default

    return current if current is not None else default


# ==========================================================
# MAIN MATCH PARSER
# ==========================================================

def parse_matches(matches, puuid):

    parsed_matches = []

    for match in matches:

        metadata = parse_metadata(safe_get(match, "metadata", default={}))

        match_id = metadata["match_id"]

        red_has_won = safe_get(match, "teams", "red", "has_won")

        players = safe_get(match, "players", "all_players", default=[])

        player_stats = parse_match_player_stats(players, puuid, match_id, red_has_won)

        rounds = safe_get(match, "rounds", default=[])

        round_data = parse_rounds(rounds, puuid, match_id)

        kill_events = extract_kill_events(match, puuid, match_id)

        parsed_matches.append({

            "metadata": metadata,
            "player_stats": player_stats,

            "rounds": round_data["rounds"],
            "damage_events": round_data["damage_events"],

            "kill_events": kill_events
        })

    return parsed_matches


# ==========================================================
# METADATA PARSER
# ==========================================================

def parse_metadata(metadata):

    return {

        "match_id": safe_get(metadata, "matchid"),
        "map": safe_get(metadata, "map"),
        "game_mode": safe_get(metadata, "mode"),

        "date_played": safe_get(metadata, "game_start_patched"),
        "game_start": safe_get(metadata, "game_start"),

        "game_length_sec": safe_get(metadata, "game_length"),
        "rounds_played": safe_get(metadata, "rounds_played"),

        "season_id": safe_get(metadata, "season_id"),
        "version": safe_get(metadata, "game_version"),
    }


# ==========================================================
# PLAYER STATS PARSER
# ==========================================================

def parse_match_player_stats(players, target_puuid, match_id, red_has_won):

    player = None

    for p in players:

        if safe_get(p, "puuid") == target_puuid:
            player = p
            break

    if player is None:
        return None

    team = safe_get(player, "team", default="").lower()

    won = red_has_won and team == "red"

    stats = safe_get(player, "stats", default={})

    return {

        "player_puuid": safe_get(player, "puuid"),
        "match_id": match_id,

        "team": team,
        "agent": safe_get(player, "character"),
        "rank": safe_get(player, "currenttier_patched"),

        "won": won,

        "kills": safe_get(stats, "kills"),
        "deaths": safe_get(stats, "deaths"),
        "assists": safe_get(stats, "assists"),

        "score": safe_get(stats, "score"),

        "damage": safe_get(player, "damage_made"),

        "headshots": safe_get(stats, "headshots"),
        "bodyshots": safe_get(stats, "bodyshots"),
        "legshots": safe_get(stats, "legshots"),

        "afk_rounds": safe_get(player, "behavior", "afk_rounds"),
        "friendly_fire_incoming": safe_get(player, "behavior", "friendly_fire", "incoming"),
        "friendly_fire_outgoing": safe_get(player, "behavior", "friendly_fire", "outgoing"),
    }


# ==========================================================
# ROUND PARSER (Single Pass)
# ==========================================================

def parse_rounds(rounds, puuid, match_id):

    rounds_table = []
    damage_events = []

    for round_number, round_data in enumerate(rounds, start=1):

        rounds_table.append(
            extract_round_summary(round_data, match_id, round_number)
        )

        damage_events.extend(
            extract_damage_events(round_data, puuid, match_id, round_number)
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
        "round_number": round_number,

        "winning_team": (safe_get(round_data, "winning_team", default="") or "").lower(),

        "round_end_reason": safe_get(round_data, "end_type"),
        
        "bomb_planted_player": safe_get(round_data, "plant_events", "planted_by", "puuid"),
        "bomb_defused_player": safe_get(round_data, "defuse_events", "defused_by", "puuid")
    }



def extract_damage_events(round_data, puuid, match_id, round_number):

    events = []

    player_stats = safe_get(round_data, "player_stats", default=[])

    for player in player_stats:

        damage_events = safe_get(player, "damage_events", default=[])
        
        attacker = safe_get(player, "player_puuid")

        for dmg in damage_events:

            receiver = safe_get(dmg, "receiver_puuid")

            if attacker == puuid or receiver == puuid:

                events.append({

                    "match_id": match_id,
                    "round_number": round_number,

                    "attacker_puuid": attacker,
                    "receiver_puuid": receiver,

                    "damage": safe_get(dmg, "damage"),
                    "headshots": safe_get(dmg, "headshots"),
                    "bodyshots": safe_get(dmg, "bodyshots"),
                    "legshot": safe_get(dmg, "legshots"),
                })

    return events


# ==========================================================
# KILL EVENT PARSER
# ==========================================================

def extract_kill_events(match, puuid, match_id):

    kill_events = safe_get(match, "kills", default=[])

    parsed = []

    for kill in kill_events:

        killer = safe_get(kill, "killer_puuid")
        victim = safe_get(kill, "victim_puuid")

        if killer == puuid or victim == puuid:

            parsed.append({

                "match_id": match_id,

                "round_number": safe_get(kill, "round"),

                "kill_time_in_round": safe_get(kill, "kill_time_in_round"),

                "killer_puuid": killer,
                "victim_puuid": victim,

                "killer_team": (safe_get(kill, "killer_team", default="") or "").lower(),
                "victim_team": (safe_get(kill, "victim_team", default="") or "").lower(),

                "weapon": safe_get(kill, "damage_weapon_name")
            })

    return parsed