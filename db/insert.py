from venv import logger
from psycopg2.extras import execute_values
from config.logging import setup_logger

import psycopg2
import logging

logger = logging.getLogger(__name__)



# ===========================================
# BULK INSERT W/ DUPLICATE PREVENTION
# ===========================================

def insert_matches(cursor, table_name, matches):
    
    query = f"""
        INSERT INTO {table_name} ( 
            match_id, 
            date_played,
            map,
            game_mode,
            season_id,
            season_name,
            act_id,
            act_name,
            game_start,
            game_length_sec,
            rounds_played
        ) VALUES %s
        ON CONFLICT (match_id) DO NOTHING;
        """

    rows = [
        (
            m["match_id"],
            m["map"],
            m["game_mode"],
            m["season_id"],
            m["season_name"],
            m["act_id"],
            m["act_name"],
            m["game_start"],
            m["game_length_sec"],
            m["rounds_played"]
        )
        for m in matches
    ]    
    
    execute_values(cursor, query, rows)
    

def insert_players(conn, players):

    query = """
        INSERT INTO players (
            puuid,
            game_name,
            tag
        ) VALUES %s
        ON CONFLICT (puuid) DO NOTHING
    """

    try:

        rows = [
            (
                p["puuid"],
                p["game_name"],
                p["tag"]
            )
            for p in players
        ]

        if not rows:
            logger.warning("No player rows to insert")
            return

        with conn.cursor() as cursor:

            execute_values(cursor, query, rows)

            inserted = cursor.rowcount
            attempted = len(rows)
            skipped = attempted - inserted

        conn.commit()

        logger.info(f"Players attempted: {attempted}")
        logger.info(f"Players inserted: {inserted}")
        logger.info(f"Players skipped (duplicates): {skipped}")

    except psycopg2.Error as e:

        conn.rollback()

        logger.error("insert_players failed")
        logger.error(e)

        raise
    
    
    
def insert_player_match_stats(cursor, table_name, stats):
    
    query = """
    INSERT INTO player_match_stats (
        match_id,
        puuid,
        team,
        agent,
        rank,
        won,
        
        kills,
        deaths,
        assists,
        score,
        damage,
        
        headhsots,
        bodyshots,
        legshots,
        
        afk_rounds,
        friendly_fire_incoming,
        friendly_fire_outgoing
    )
    VALUES %s
    ON CONFLICT (match_id, player_puuid) DO NOTHING
    """

    rows = [
        (
            s["match_id"],
            s["puuid"],
            s["team"],
            s["agent"],
            s["rank"],
            s["won"],
            s["kills"],
            s["deaths"],
            s["assists"],
            s["score"],
            s["damage"],
            s["headhsots"],
            s["bodyshots"],
            s["legshots"],
            s["afk_rounds"],
            s["friendly_fire_incoming"],
            s["friendly_fire_outgoing"]
        )
        for s in stats
    ]

    execute_values(cursor, query, rows)

def insert_rounds(cursor, table_name, rounds):
    
    query = f"""
        INSERT INTO {table_name} ( 
            match_id, 
            round_number,
            winning_team,
            round_end_reason,
            bomb_planted_player,
            bomb_defused_player
        ) VALUES %s
        ON CONFLICT (match_id, round_number) DO NOTHING;
        """

    rows = [
        (
            r["match_id"],
            r["round_number"],
            r["winning_team"],
            r["round_end_reason"],
            r["bomb_planted_player"],
            r["bomb_defused_player"]
        )
        for r in rounds
    ]    
    
    execute_values(cursor, query, rows)
    
    
def insert_damage_events(cursor, table_name, dmg_events):
    
    query = f"""
        INSERT INTO {table_name} ( 
            match_id, 
            round_number,
            attacker_puuid,
            receiver_puuid,
            damage,
            headhsots,
            bodyshots,
            legshots
        ) VALUES %s
        ON CONFLICT (
            match_id,
            round_number,
            attacker_puuid,
            receiver_puuid
        ) DO NOTHING
        """

    rows = [
        (
            dmg["match_id"],
            dmg["round_number"],
            dmg["attacker_puuid"],
            dmg["receiver_puuid"],
            dmg["damage"],
            dmg["headhsots"],
            dmg["bodyshots"],
            dmg["legshots"]
        )
        for dmg in dmg_events
    ]    
    
    execute_values(cursor, query, rows)
    
    
def insert_kill_events(cursor, table_name, kills):
    query = f"""
        INSERT INTO {table_name} ( 
            match_id, 
            round_number,
            killer_puuid,
            victim_puuid,
            damage,
            killer_team,
            victim_team,
            weapon
        ) VALUES %s
        ON CONFLICT (
            match_id,
            round_number,
            kill_time_in_round,
            killer_puuid,
            victim_puuid
        ) DO NOTHING
        """

    rows = [
        (
            k["match_id"],
            k["round_number"],
            k["attacker_puuid"],
            k["receiver_puuid"],
            k["damage"],
            k["headhsots"],
            k["bodyshots"],
            k["legshots"]
        )
        for k in kills
    ]    
    
    execute_values(cursor, query, rows)



def insert_damamge_events(engine, table_name, data):
    if not data:
        logger.info(f"No event data to insert into {table_name}")
        return 0
    
    return 1 # number of records inserted
    
def insert_kill_events(engine, table_name, data):
    if not data:
        logger.info(f"No kill event data to insert into {table_name}")
        return 0
    
    return 1 # number of records inserted
    
    
def insert_session_data(engine, table_name, data):
    if not data:
        logger.info(f"No session data to insert into {table_name}")
        return 0
    
    return 1 # number of records inserted

def insert_session_matches(engine, table_name, data):
    if not data:
        logger.info(f"No session match data to insert into {table_name}")
        return 0
    
    return 1 # number of records inserted

    
    
# ===========================================
# Queries
# ===========================================
# * fetch matches by season (if season is given, filter by season column for matches. if no season is given, default to current season)
# * fetch match stats
# * fetch rounds
# * fetch player info and stats
# * fetch kill events
# * fetch damage events

# if no season is given, default to curent. if season is given, fetch data for that season. 
# (filer by season column for matches)

def fetch_matches_by_season(engine, puuid, season):
    
    return pd.DataFrame()
