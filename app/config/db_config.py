import psycopg2

def get_db_connection():
    return psycopg2.connect(
        host="",
        port="5432",
        user="neondb_owner",
        password="",
        dbname="neondb"
    )
