import psycopg2
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.contract_types_model import contract_types
from fastapi.encoders import jsonable_encoder
class contract_types_controller():
    def create_contract_type(self,contract_type:contract_types):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO contract_types(contract_name,description,duration) VALUES (%s,%s,%s)",(contract_type.contract_name,contract_type.description,contract_type.duration))
            conn.commit()
            return {"message":"Contract type created"}
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()
    def get_contract_types(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM contract_types")
            result = cursor.fetchall()
            if result:
                return result
            else:
                raise HTTPException(status_code=404, detail="contract types not found")
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()

    def get_contract_type(self,id_contract_type:int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM contract_types WHERE id_type = %s", (id_contract_type,))
            result = cursor.fetchone()
            if result:
                return result
            else:
                raise HTTPException(status_code=404, detail="contract type not found")
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()
    def edit_contract_type(self, contract_type_id:int,contract_types:contract_types):
        try:
            conn =get_db_connection()
            cursor=conn.cursor()
            query="update contract_types set contract_name=%s,description=%s,duration=%s where id_type=%s"
            values=(contract_types.contract_name,contract_types.description,contract_types.duration,contract_type_id)
            cursor.execute(query,values)
            conn.commit()
            return {"message":"Contract type updated"}
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()
    def delete_contract_type(self,id_contract_type:int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM contract_types WHERE id_type = %s", (id_contract_type,))
            conn.commit()
            return {"message": "contract type deleted successfully"}
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()