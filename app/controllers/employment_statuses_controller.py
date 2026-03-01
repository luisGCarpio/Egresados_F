import psycopg2
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.employment_statuses_model import employment_statuses
from fastapi.encoders import jsonable_encoder

class employment_statuses_controller():

    def create_employment_status(self, employment_status: employment_statuses):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO employment_statuses (description) VALUES (%s)", (employment_status.description,))
            conn.commit()
            return {"message": "employment status created successfully"}
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()
    def get_employment_status(self, id_status: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM employment_statuses WHERE id_status = %s", (id_status,))
            result = cursor.fetchone()
            if result:
                return result
            else:
                raise HTTPException(status_code=404, detail="employment status not found")
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()
    def get_employment_statuses(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM employment_statuses")
            result = cursor.fetchall()
            if result:
                return result
            else:
                raise HTTPException(status_code=404, detail="employment status not found")
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()
    def edit_employment_status(self, id_status: int, employment_status: employment_statuses):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE employment_statuses SET description = %s WHERE id_status = %s", (employment_status.description, id_status))
            conn.commit()
            return {"message": "employment status updated successfully"}
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()
    def delete_employment_status(self, id_status: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM employment_statuses WHERE id_status = %s", (id_status,))
            conn.commit()
            return {"message": "employment status deleted successfully"}
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()
            