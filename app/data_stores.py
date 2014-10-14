import os
import psycopg2

from app_config import Config

pg_conn = psycopg2.connect(database=Config.POSTGRES_DB,
                            user=Config.POSTGRES_USER, 
                            password=Config.POSTGRES_PASS,
                            host=Config.POSTGRES_HOST,
                            port=int(Config.POSTGRES_PORT))

# NOTE make sure tables are properly set up ... PG isn't quite as easy as redis :)
import tables

