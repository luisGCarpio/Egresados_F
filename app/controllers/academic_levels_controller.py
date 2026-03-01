import psycopg2
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.academic_levels_model import academic_levels
from fastapi.encoders import jsonable_encoder

class academic_levels_controller():
    def create_academic_level(self, AcademicLevel: academic_levels):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO academic_levels (description) VALUES (%s)", (AcademicLevel.description,))
            conn.commit()
            conn.close()
            return {"resultado": "Nivel academico creado"}
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()
    def get_academic_level(self, id_level: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM academic_levels WHERE id_level = %s", (id_level,))
            result = cursor.fetchone()
            if result:
                return result
            else:
                raise HTTPException(status_code=404, detail="academic level not found")
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()
    def get_academic_levels(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM academic_levels")
            result = cursor.fetchall()
            if result:
                return result
            else:
                raise HTTPException(status_code=404, detail="academic level not found")
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()
    def edit_academic_level(self, id_level: int, AcademicLevel: academic_levels):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE academic_levels SET description = %s WHERE id_level = %s", (AcademicLevel.description, id_level))
            conn.commit()
            conn.close()
            return {"resultado": "Nivel academico actualizado"}
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()
    def delete_academic_level(self, id_level: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM academic_levels WHERE id_level = %s", (id_level,))
            conn.commit()
            return {"message": "academic level deleted successfully"}
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()