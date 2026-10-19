import sqlite3
import psycopg2

# path / url de conexão
DB_PATH = "postgresql://neondb_owner:npg_MbrmkL7xN5wU@ep-cool-snow-b8arbmtk-pooler.c-14.us-east-1.aws.neon.tech/neondb?channel_binding=require&sslmode=require"

def get_connection():
    return psycopg2.connect(DB_PATH)