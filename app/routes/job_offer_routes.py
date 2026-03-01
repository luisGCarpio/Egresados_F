from fastapi import APIRouter, HTTPException
from controllers.job_offer_controller import *

from models.job_offer_model import job_offer

router = APIRouter()

new_job_offer = job_offer_controller()

@router.post("/create_job_offer")
async def create_job_offer(job_offer: job_offer):
    return new_job_offer.create_job_offer(job_offer)

@router.get("/get_job_offers")
async def get_job_offers():
    return new_job_offer.get_job_offers()

@router.get("/get_job_offer/{id_job_offer}")
async def get_job_offer(id_job_offer: int):
    return new_job_offer.get_job_offer(id_job_offer)

@router.put("/edit_job_offer/{id_job_offer}")
async def edit_job_offer(id_job_offer: int, job_offer: job_offer):
    return new_job_offer.edit_job_offer(id_job_offer, job_offer)

@router.delete("/delete_job_offer/{id_job_offer}")
async def delete_job_offer(id_job_offer: int):
    return new_job_offer.delete_job_offer(id_job_offer)