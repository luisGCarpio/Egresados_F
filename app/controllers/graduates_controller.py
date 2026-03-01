import psycopg2
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.graduates_model import graduates
from fastapi.encoders import jsonable_encoder

class graduates_controller:
    def create_graduates(self, graduates: graduates):
        try:
            conn=get_db_connection()
            cursor=conn.cursor()
            querry="INSERT INTO graduates (first_name, last_name, email, phone, birth_date, graduation_year, id_level, id_status, id_program) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            vars=(graduates.first_name, graduates.last_name, graduates.email, graduates.phone, graduates.birth_date, graduates.graduation_year, graduates.id_level, graduates.id_status, graduates.id_program)  
            cursor.execute(querry, vars)
            conn.commit()
            cursor.close()
            return {"resultado": "graduates creado"}
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()
    def get_graduate(self, id_graduate: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM graduates WHERE id_graduate = %s", (id_graduate,))
            result = cursor.fetchone()
            if result:
                return result
            else:
                raise HTTPException(status_code=404, detail="graduates not found")
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()
    def get_graduates(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM graduates")
            result = cursor.fetchall()
            if result:
                return result
            else:
                raise HTTPException(status_code=404, detail="graduates not found")
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()
    def edit_graduate(self, graduates: graduates, id_graduate: int):
        try:
            conn=get_db_connection()
            cursor=conn.cursor()
            querry="UPDATE graduates SET first_name = %s, last_name = %s, email = %s, phone = %s, birth_date = %s, graduation_year = %s, id_level = %s, id_status = %s, id_program = %s WHERE id_graduate = %s"
            values=(graduates.first_name, graduates.last_name, graduates.email, graduates.phone, graduates.birth_date, graduates.graduation_year, graduates.id_level, graduates.id_status, graduates.id_program, id_graduate)
            cursor.execute(querry, values)
            conn.commit()
            cursor.close()
            return {"resultado": "graduates editado"}
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def delete_graduate(self, id_graduate: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM graduates WHERE id_graduate = %s", (id_graduate,))
            conn.commit()
            cursor.close()
            return {"resultado": "graduates eliminado"}
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()