from venv import logger
from psycopg2.extras import execute_values

import psycopg2
import logging

logger = logging.getLogger(__name__)



# ===========================================
# BULK INSERT W/ DUPLICATE PREVENTION
# ===========================================

def insert_matches(conn, matches):
    
    query = f"""
        INSERT INTO matches ( 
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

    try: 
        rows = [
            (
                m["match_id"],
                m["date_played"],
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
        
        if not rows:
            logger.warning("No matches to insert")
            return
        
        
        with conn.cursor() as cursor:

            execute_values(cursor, query, rows)

            inserted = cursor.rowcount
            attempted = len(rows)
            skipped = attempted - inserted

        conn.commit()

        logger.info(f"Matches attempted: {attempted} | kill events inserted: {inserted} | kill events skipped (duplicates): {skipped}")

    except psycopg2.Error as e:

        conn.rollback()

        logger.error("insert_matches failed")
        logger.error(e)

        raise
        
        
    

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
            logger.warning("No players to insert")
            return

        with conn.cursor() as cursor:

            execute_values(cursor, query, rows)

            inserted = cursor.rowcount
            attempted = len(rows)
            skipped = attempted - inserted

        conn.commit()

        logger.info(f"Players attempted: {attempted} | kill events inserted: {inserted} | kill events skipped (duplicates): {skipped}")

    except psycopg2.Error as e:

        conn.rollback()

        logger.error("insert_players failed")
        logger.error(e)

        raise
    
    
    
def insert_player_match_stats(conn, stats):
    
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
        
        headshots,
        bodyshots,
        legshots,
        
        afk_rounds,
        friendly_fire_incoming,
        friendly_fire_outgoing
    )
    VALUES %s
    ON CONFLICT (match_id, puuid) DO NOTHING
    """

    try:
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
                s["headshots"],
                s["bodyshots"],
                s["legshots"],
                s["afk_rounds"],
                s["friendly_fire_incoming"],
                s["friendly_fire_outgoing"]
            )
            for s in stats
        ]

        if not rows:
            logger.warning("No player match stats to insert")
            return

        with conn.cursor() as cursor:

            execute_values(cursor, query, rows)

            inserted = cursor.rowcount
            attempted = len(rows)
            skipped = attempted - inserted

        conn.commit()

        logger.info(f"Player match stats attempted: {attempted} | kill events inserted: {inserted} | kill events skipped (duplicates): {skipped}")

    except psycopg2.Error as e:

        conn.rollback()

        logger.error("insert_player_match_stats failed")
        logger.error(e)

        raise

def insert_rounds(conn, rounds):
    
    query = f"""
        INSERT INTO rounds ( 
            match_id, 
            round_number,
            winning_team,
            round_end_reason,
            bomb_planted_player,
            bomb_defused_player
        ) VALUES %s
        ON CONFLICT (match_id, round_number) DO NOTHING;
        """
    
    try:
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
        
        if not rows:
            logger.warning("No rounds to insert")
            return

        with conn.cursor() as cursor:

            execute_values(cursor, query, rows)

            inserted = cursor.rowcount
            attempted = len(rows)
            skipped = attempted - inserted

        conn.commit()

        logger.info(f"Rounds attempted: {attempted} | kill events inserted: {inserted} | kill events skipped (duplicates): {skipped}")

    except psycopg2.Error as e:

        conn.rollback()

        logger.error("insert_rounds failed")
        logger.error(e)

        raise
    
    
def insert_damage_events(conn, dmg_events):
    
    query = f"""
        INSERT INTO damage_events ( 
            match_id, 
            round_number,
            attacker_puuid,
            receiver_puuid,
            damage,
            headshots,
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

    try:
        rows = [
            (
                dmg["match_id"],
                dmg["round_number"],
                dmg["attacker_puuid"],
                dmg["receiver_puuid"],
                dmg["damage"],
                dmg["headshots"],
                dmg["bodyshots"],
                dmg["legshots"]
            )
            for dmg in dmg_events
        ]
        
        
        if not rows:
            logger.warning("No damage events to insert")
            return

        with conn.cursor() as cursor:

            execute_values(cursor, query, rows)

            inserted = cursor.rowcount
            attempted = len(rows)
            skipped = attempted - inserted

        conn.commit()

        logger.info(f"Damage events attempted: {attempted} | kill events inserted: {inserted} | kill events skipped (duplicates): {skipped}")

    except psycopg2.Error as e:

        conn.rollback()

        logger.error("insert_damage_events failed")
        logger.error(e)

        raise
    
    
def insert_kill_events(conn, kills):
    query = f"""
        INSERT INTO kill_events ( 
            match_id, 
            round_number,
            kill_time_in_round,
            killer_puuid,
            victim_puuid,
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

    try:
        rows = [
            (
                k["match_id"],
                k["round_number"],
                k["kill_time_in_round"],
                k["killer_puuid"],
                k["victim_puuid"],
                k["killer_team"],
                k["victim_team"],
                k["weapon"]
            )
            for k in kills
        ]    
        
        if not rows:
            logger.warning("No kill events to insert")
            return

        with conn.cursor() as cursor:

            execute_values(cursor, query, rows)

            inserted = cursor.rowcount
            attempted = len(rows)
            skipped = attempted - inserted

        conn.commit()

        logger.info(f"kill events attempted: {attempted} | kill events inserted: {inserted} | kill events skipped (duplicates): {skipped}")

    except psycopg2.Error as e:

        conn.rollback()

        logger.error("insert_kill_events failed")
        logger.error(e)

        raise


def insert_episodes(conn, episodes):
    
    query = f"""
        INSERT INTO episodes ( 
            episode_id,
            episode_name
        ) VALUES %s
        ON CONFLICT (episode_id) DO NOTHING
        """

    try:
        rows = [
            (
                e["episode_id"],
                e["episode_name"]
            )
            for e in episodes
        ]    
        
        if not rows:
            logger.warning("No episodes to insert")
            return

        with conn.cursor() as cursor:

            execute_values(cursor, query, rows)

            inserted = cursor.rowcount
            attempted = len(rows)
            skipped = attempted - inserted

        conn.commit()

        logger.info(f"Episodes attempted: {attempted} | Episodes inserted: {inserted} | Episodes skipped (duplicates): {skipped}")

    except psycopg2.Error as e:

        conn.rollback()

        logger.error("insert_episodes failed")
        logger.error(e)

        raise
    
    
def insert_acts(conn, acts):
    
    query = f"""
        INSERT INTO acts ( 
            act_id,
            act_name,
            episode_id,
            is_active,
            is_previous
        ) VALUES %s
        ON CONFLICT (act_id) DO NOTHING
        """

    try:
        rows = [
            (
                a["act_id"],
                a["act_name"],
                a["episode_id"],
                a["is_active"],
                a["is_previous"]
            )
            for a in acts
        ]    
        
        if not rows:
            logger.warning("No acts to insert")
            return

        with conn.cursor() as cursor:

            execute_values(cursor, query, rows)

            inserted = cursor.rowcount
            attempted = len(rows)
            skipped = attempted - inserted

        conn.commit()

        logger.info(f"Acts attempted: {attempted} | Acts inserted: {inserted} | Acts skipped (duplicates): {skipped}")

    except psycopg2.Error as e:

        conn.rollback()

        logger.error("insert_acts failed")
        logger.error(e)

        raise