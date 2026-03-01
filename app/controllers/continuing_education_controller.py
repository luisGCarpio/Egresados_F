import psycopg2
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.continuing_education_model import continuing_education
from fastapi.encoders import jsonable_encoder

class continuing_education_controller:
    def create_continuing_education(self, data: continuing_education):
        conn = None
        try:
            conn = get_db_connection()
            with conn.cursor() as cursor:
                query = """
                    INSERT INTO continuing_education 
                    (id_graduate, description_program, education_type, time, education_date)
                    VALUES (%s, %s, %s, %s, %s)
                    RETURNING id_continuing_education, id_graduate, description_program, education_type, time, education_date
                """
                values = (
                    data.id_graduate,
                    data.description_program,
                    data.education_type,
                    data.time,
                    data.education_date
                )
                cursor.execute(query, values)
                result = cursor.fetchone()
                conn.commit()

                if result:
                    return {
                        "id_continuing_education": result[0],
                        "id_graduate": result[1],
                        "description_program": result[2],
                        "education_type": result[3],
                        "time": result[4],
                        "education_date": result[5]
                    }

        except psycopg2.Error as err:
            if conn:
                conn.rollback()
            # Imprime en consola para ti y devuelve el detalle al cliente
            print(f"Error de Postgres: {err.pgcode} - {err.pgerror}")
            raise HTTPException(status_code=500, detail=str(err.pgerror))
        finally:
            if conn:
                conn.close()
    def get_continuing_education(self):
        try:
            connection = get_db_connection()
            cursor = connection.cursor()
            query = "SELECT * FROM continuing_education"
            cursor.execute(query)
            result = cursor.fetchall()
            if result:
                return result
            else:
                raise HTTPException(status_code=404, detail="Continuing education not found")
        except psycopg2.Error as err:
            print(err)
            connection.rollback()
        finally:
            cursor.close()
            connection.close()
    def get_continuing_education_by_id(self, id_continuing_education):
        try:
            connection = get_db_connection()
            cursor = connection.cursor()
            query = "SELECT * FROM continuing_education WHERE id_continuing_education = %s"
            cursor.execute(query, (id_continuing_education,))
            result = cursor.fetchone()
            if result:
                return result
            else:
                raise HTTPException(status_code=404, detail="Continuing education not found")
        except psycopg2.Error as err:
            print(err)
            connection.rollback()
        finally:
            cursor.close()
            connection.close()
    def edit_continuing_education(self, id_continuing_education, continuing_education:continuing_education):
        try:
            connection = get_db_connection()
            cursor = connection.cursor()
            query = "UPDATE continuing_education SET description_program = %s, education_type = %s, time = %s, education_date = %s WHERE id_continuing_education = %s"
            values = (continuing_education.description_program, continuing_education.education_type, continuing_education.time, continuing_education.education_date, id_continuing_education)
            cursor.execute(query, values)
            connection.commit()
            cursor.close()
            connection.close()
            return {"message": "Continuing education updated successfully"}
        except psycopg2.Error as err:
            print(err)
            connection.rollback()
        finally:
            connection.close()
    def delete_continuing_education(self, id_continuing_education):
        try:
            connection = get_db_connection()
            cursor = connection.cursor()
            query = "DELETE FROM continuing_education WHERE id_continuing_education = %s"
            cursor.execute(query, (id_continuing_education,))
            connection.commit()
            cursor.close()
            connection.close()
            return {"message": "Continuing education deleted successfully"}
        except psycopg2.Error as err:
            print(err)
            connection.rollback()
        finally:
            connection.close()