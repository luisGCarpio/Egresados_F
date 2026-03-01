import psycopg2
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.jobs_model import jobs
from fastapi.encoders import jsonable_encoder

class jobs_controller:
    def create_job(self, job: jobs): # Asumiendo que 'jobs' es tu modelo Pydantic
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            
            # El INSERT coincide exactamente con las columnas de tu tabla SQL
            query = """
                INSERT INTO jobs (
                    id_graduate, company, id_sector, position, salary, 
                    start_date, end_date, id_type, related_to_career
                ) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            
            # Los valores coinciden exactamente con el orden del query de arriba
            values = (
                job.id_graduate,
                job.company,
                job.id_sector,
                job.position,
                job.salary,
                job.start_date,
                job.end_date,
                job.id_type,
                job.related_to_career
            )
            
            cursor.execute(query, values)
            conn.commit()
            cursor.close()
            
            return {"Resultado": "Job created successfully"}

        except psycopg2.Error as err:
            if conn:
                conn.rollback()
            print(f"Error de Base de Datos: {err}")
            # Esto mostrará el error real en Swagger si algo falla
            raise HTTPException(status_code=500, detail=str(err))
            
        except Exception as e:
            if conn:
                conn.rollback()
            print(f"Error de Código: {e}")
            raise HTTPException(status_code=500, detail=str(e))
            
        finally:
            if conn:
                conn.close()
       
    def get_jobs(self):
        try:
            conn=get_db_connection()
            cursor=conn.cursor()
            cursor.execute("select * from jobs")
            jobs=cursor.fetchall()
            cursor.close()
            return jobs
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def get_job(self,id_job:int):
        try:
            conn=get_db_connection()
            cursor=conn.cursor()
            cursor.execute("select * from jobs where id_job=%s", (id_job,))
            job=cursor.fetchone()
            cursor.close()
            return job
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()
    def edit_job(self, id_job: int, job: jobs):
        conn = None
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            
            # 1. Query con las columnas REALES de tu tabla
            query = """
                UPDATE jobs 
                SET id_graduate=%s, company=%s, id_sector=%s, position=%s, 
                    salary=%s, start_date=%s, end_date=%s, id_type=%s, 
                    related_to_career=%s 
                WHERE id_job=%s
            """
            
            # 2. Valores que coinciden con tu modelo de Pydantic
            values = (
                job.id_graduate,
                job.company,
                job.id_sector,
                job.position,
                job.salary,
                job.start_date,
                job.end_date,
                job.id_type,
                job.related_to_career,
                id_job  # El ID que viene por la URL
            )
            
            cursor.execute(query, values)
            conn.commit()
            cursor.close()
            
            return {"Resultado": "Job updated successfully"}

        except Exception as err:
            if conn:
                conn.rollback()
            print(f"Error: {err}")
            from fastapi import HTTPException
            # Esto te mostrará el error real en Swagger
            raise HTTPException(status_code=500, detail=str(err))
        finally:
            if conn:
                conn.close()
    def delete_job(self,id_job:int):
        try:
            conn=get_db_connection()
            cursor=conn.cursor()
            cursor.execute("delete from jobs where id_job=%s", (id_job,))
            conn.commit()
            cursor.close()
            return{"Resultado":"Job deleted"}
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()