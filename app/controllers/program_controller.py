import psycopg2
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.program_model import program
from fastapi.encoders import jsonable_encoder

class proram_controller:
        
    def create_program(self, Program: program):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO program (program_name, faculty) VALUES ( %s ,%s)", (Program.program_name, Program.faculty))
            conn.commit()
            conn.close()
            return {"resultado": "Programa creado"}
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()
        
    def get_program(self, program_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM program WHERE id_program = %s", (program_id,))
            result = cursor.fetchone()
            payload = []
            content = {} 
            
            content={
                    'id':int(result[0]),
                    'name':result[1],
                    'faculty':result[2]
            }
            payload.append(content)
            
            json_data = jsonable_encoder(content)            
            if result:
               return  json_data
            else:
                raise HTTPException(status_code=404, detail="program not found")  
                
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()
       
    def get_programs(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM program")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'id':data[0],
                    'name':data[1],
                    'faculty':data[2]
                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)        
            if result:
               return {"resultado": json_data}
            else:
                raise HTTPException(status_code=404, detail="program not found")  
                
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()
    def edit_program(self, program_id: int, Program: program):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE program SET program_name = %s, faculty = %s WHERE id_program = %s", (Program.program_name, Program.faculty, program_id))
            conn.commit()
            conn.close()
            return {"resultado": "Programa actualizado"}
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()
    def delete_program(self, program_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM program WHERE id_program = %s", (program_id,))
            conn.commit()
            conn.close()
            return {"resultado": "Programa eliminado"}
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()