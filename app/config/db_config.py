import psycopg2

def get_db_connection():
    return psycopg2.connect(
        host="ep-soft-poetry-aiwbf4xr-pooler.c-4.us-east-1.aws.neon.tech",
        port="5432",
        user="neondb_owner",
        password="npg_oYl5KdXygC8E",
        dbname="neondb"
    )
#psql 'postgresql://neondb_owner:npg_oYl5KdXygC8E@ep-soft-poetry-aiwbf4xr-pooler.c-4.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require'