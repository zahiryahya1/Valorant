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
from venv import logger
from psycopg2.extras import execute_values

import psycopg2
import logging


logger = logging.getLogger(__name__)


def get_current_season(conn):
    
    query = """
        SELECT
            act_id AS act_id
        FROM acts
        WHERE is_active = TRUE
    """
    
    cursor = conn.cursor()
    cursor.execute(query)   
        
    row = cursor.fetchone()

    if row is None:
        logger.warning("No active season found in database")
        return None     
    
    season_id = row[0]
    
    logger.info(f"Current season id retrieved: {season_id}")
    
    return season_id
    
    
def get_previous_season(conn):
    
    query = """
        SELECT
            act_id AS act_id
        FROM acts
        WHERE is_previous = TRUE
    """
    
    cursor = conn.cursor()
    cursor.execute(query)   
        
    row = cursor.fetchone()

    if row is None:
        logger.warning("No active season found in database")
        return None     
    
    season_id = row[0]
    
    logger.info(f"Current season id retrieved: {season_id}")
    
    return season_id
    