import psycopg2
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.work_supervisor_model import work_supervisor
from fastapi.encoders import jsonable_encoder

class work_supervisor_controller:
    def create_work_supervisor(self, work_supervisor: work_supervisor):
        try:
            db = get_db_connection()
            cursor = db.cursor()
            query = "INSERT INTO work_supervisor (id_program, nombre_profesor, id_graduate, first_name, id_job) VALUES (%s, %s, %s, %s, %s)"
            values = (work_supervisor.id_program, work_supervisor.nombre_profesor, work_supervisor.id_graduate, work_supervisor.first_name, work_supervisor.id_job)
            cursor.execute(query, values)
            db.commit()
            return {"message": "work_supervisor created successfully"}
        except (Exception, psycopg2.Error) as error:
            print("Error al crear el work_supervisor:", error)
            raise HTTPException(status_code=500, detail="Error al crear el work_supervisor")
        finally:
            cursor.close()
            db.close()
    def get_work_supervisors(self):
        try:
            db = get_db_connection()
            cursor = db.cursor()
            query = "SELECT * FROM work_supervisor"
            cursor.execute(query)
            work_supervisors = cursor.fetchall()
            return work_supervisors
        except (Exception, psycopg2.Error) as error:
            print("Error al obtener los work_supervisors:", error)
            raise HTTPException(status_code=500, detail="Error al obtener los work_supervisors")
        finally:
            cursor.close()
            db.close()
    def get_work_supervisor(self, id_supervisor: int):
        try:
            db = get_db_connection()
            cursor = db.cursor()
            query = "SELECT * FROM work_supervisor WHERE id_supervisor = %s"
            cursor.execute(query, (id_supervisor,))
            work_supervisor = cursor.fetchone()
            return work_supervisor
        except (Exception, psycopg2.Error) as error:
            print("Error al obtener el work_supervisor:", error)
            raise HTTPException(status_code=500, detail="Error al obtener el work_supervisor")
        finally:
            cursor.close()
            db.close()
    def edit_work_supervisor(self, id_supervisor: int, work_supervisor: work_supervisor):
        try:
            db = get_db_connection()
            cursor = db.cursor()
            query = "UPDATE work_supervisor SET id_program = %s, nombre_profesor = %s, id_graduate = %s, first_name = %s, id_job = %s WHERE id_supervisor = %s"
            values = (work_supervisor.id_program, work_supervisor.nombre_profesor, work_supervisor.id_graduate, work_supervisor.first_name, work_supervisor.id_job, id_supervisor)
            cursor.execute(query, values)
            db.commit()
            return work_supervisor
        except (Exception, psycopg2.Error) as error:
            print("Error al editar el work_supervisor:", error)
            raise HTTPException(status_code=500, detail="Error al editar el work_supervisor")
        finally:
            cursor.close()
            db.close()
    def delete_work_supervisor(self, id_supervisor: int):
        try:
            db = get_db_connection()
            cursor = db.cursor()
            query = "DELETE FROM work_supervisor WHERE id_supervisor = %s"
            cursor.execute(query, (id_supervisor,))
            db.commit()
            return {"message": "work_supervisor deleted successfully"}
        except (Exception, psycopg2.Error) as error:
            print("Error al eliminar el work_supervisor:", error)
            raise HTTPException(status_code=500, detail="Error al eliminar el work_supervisor")
        finally:
            cursor.close()
            db.close()