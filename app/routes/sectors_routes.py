from fastapi import APIRouter, HTTPException
from controllers.sectors_controller import *

from models.sectors_model import sectors

router = APIRouter()

new_sector = sectors_controller()

@router.post("/create_sector")
async def create_sector(sector: sectors):
    return new_sector.create_sector(sector)

@router.get("/get_sectors")
async def get_sectors():
    return new_sector.get_sectors()

@router.get("/get_sector/{id_sector}")
async def get_sector(id_sector: int):
    return new_sector.get_sector(id_sector)

@router.put("/edit_sector/{id_sector}")
async def edit_sector(id_sector: int, sector: sectors):
    return new_sector.edit_sector(id_sector, sector)

@router.delete("/delete_sector/{id_sector}")
async def delete_sector(id_sector: int):
    return new_sector.delete_sectors(id_sector)