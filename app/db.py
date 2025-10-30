import psycopg2
from psycopg2.extras import RealDictCursor
import os
from dotenv import load_dotenv

load_dotenv()

def get_db_connection():
    try:
        # Add some debugging
        print(f"Connecting to: host={os.getenv('DB_HOST')}, db={os.getenv('DB_NAME')}, user={os.getenv('DB_USER')}")
        
        conn = psycopg2.connect(
            host=os.getenv("DB_HOST"),
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            port=os.getenv("DB_PORT", 5432)  # Add port with default
        )
        print("Database connection successful!")
        return conn
    except Exception as e:
        print(f"Database connection failed: {e}")
        raise e

