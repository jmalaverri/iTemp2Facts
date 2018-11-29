import psycopg2
from config import config

class Database:
    @staticmethod
    def connect_dbs():
        
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        
        return conn