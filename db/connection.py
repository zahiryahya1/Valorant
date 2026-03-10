import psycopg2
import os
import logging

from dotenv import load_dotenv
from config.logging import setup_logger

load_dotenv()
logger = logging.getLogger(__name__)

# ===========================================
# DATABASE CONNECTION
# ===========================================

def get_connection():
    """Return psycopg2 connection for PostgreSQL."""
    db_user = os.getenv("DB_USER")
    db_pass = os.getenv("DB_PASSWORD")
    db_host = os.getenv("DB_HOST")
    db_port = os.getenv("DB_PORT")
    db_name = os.getenv("DB_NAME")

    try:
        conn = psycopg2.connect(
            host=db_host,
            port=db_port,
            database=db_name,
            user=db_user,
            password=db_pass
        )
        
        logger.info("Database connection established successfully")
        return conn

    except Exception as e:
        logger.error(f"Database connection failed: {e}")
        raise
    
    
