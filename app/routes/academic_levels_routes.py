from fastapi import APIRouter, HTTPException
from controllers.academic_levels_controller import *

from models.academic_levels_model import academic_levels

router = APIRouter()

new_academic_level = academic_levels_controller()

@router.post("/create_academic_level")
async def create_academic_level(AcademicLevel: academic_levels):
    return new_academic_level.create_academic_level(AcademicLevel)
@router.get("/get_academic_levels")
async def get_academic_levels():
    return new_academic_level.get_academic_levels()

@router.get("/get_academic_level/{id_level}")
async def get_academic_level(id_level: int):
    return new_academic_level.get_academic_level(id_level)

@router.put("/edit_academic_level/{id_level}")
async def edit_academic_level(id_level: int, AcademicLevel: academic_levels):
    return new_academic_level.edit_academic_level(id_level, AcademicLevel)

@router.delete("/delete_academic_level/{id_level}")
async def delete_academic_level(id_level: int):
    return new_academic_level.delete_academic_level(id_level)