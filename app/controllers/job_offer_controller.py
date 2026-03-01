import psycopg2
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.job_offer_model import job_offer
from fastapi.encoders import jsonable_encoder

class job_offer_controller:
    def create_job_offer(self, job_offer: job_offer):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            query = "INSERT INTO job_offer (position, company, salary, id_type, area, email_contact, offer_date) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            values=(job_offer.position, job_offer.company, job_offer.salary, job_offer.id_type, job_offer.area, job_offer.email_contact, job_offer.offer_date)
            cursor.execute(query, values)
            conn.commit()
            conn.close()
            return {"resultado": "job offer creado"}
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()
    def get_job_offers(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM job_offer")
            job_offers = cursor.fetchall()
            conn.close()
            return job_offers
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()
    def get_job_offer(self, id_job_offer: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM job_offer WHERE id_offer = %s", (id_job_offer,))
            job_offer = cursor.fetchone()
            conn.close()
            return job_offer
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()
    def edit_job_offer(self,id_job_offer: int, job_offer: job_offer):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            query = "UPDATE job_offer SET position = %s, company = %s, salary = %s, id_type = %s, area = %s, email_contact = %s, offer_date = %s WHERE id_offer = %s"
            values = (job_offer.position, job_offer.company, job_offer.salary, job_offer.id_type, job_offer.area, job_offer.email_contact, job_offer.offer_date, id_job_offer)
            cursor.execute(query, values)
            conn.commit()
            conn.close()
            return {"resultado": "job offer actualizado"}
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()
    def delete_job_offer(self, id_job_offer: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM job_offer WHERE id_offer = %s", (id_job_offer,))
            conn.commit()
            conn.close()
            return {"resultado": "job offer eliminado"}
        except psycopg2.Error as err:
            print(err)
            conn.rollback()
        finally:
            conn.close()