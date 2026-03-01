import psycopg2
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.sectors_model import sectors
from fastapi.encoders import jsonable_encoder

class sectors_controller:
    def create_sector(self, sector: sectors):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO sectors (name) VALUES (%s)", (sector.name,))
            conn.commit()
            return {"message": "sector created successfully"}
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()
    def get_sectors(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM sectors")
            result = cursor.fetchall()
            if result:
                return result
            else:
                raise HTTPException(status_code=404, detail="sectors not found")
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()
    def get_sector(self, id_sector: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM sectors WHERE id_sector = %s", (id_sector,))
            result = cursor.fetchone()
            if result:
                return result
            else:
                raise HTTPException(status_code=404, detail="sector not found")
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()
    def edit_sector(self,id_sector:int, sector: sectors):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE sectors SET name = %s WHERE id_sector = %s", (sector.name, id_sector))
            conn.commit()
            return {"message": "sector updated successfully"}
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()
    def delete_sectors(self, id_sector: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM sectors WHERE id_sector = %s", (id_sector,))
            conn.commit()
            return {"message": "sector deleted successfully"}
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()