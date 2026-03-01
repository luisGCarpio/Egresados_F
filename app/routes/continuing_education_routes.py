from fastapi import APIRouter, HTTPException
from controllers.continuing_education_controller import *

from models.continuing_education_model import continuing_education

router = APIRouter()

new_continuing_education = continuing_education_controller()
@router.post("/create_continuing_education")
async def create_continuing_education(continuing_education: continuing_education):    
    return new_continuing_education.create_continuing_education(continuing_education)

@router.get("/get_continuing_education")
async def get_continuing_education():    
    return new_continuing_education.get_continuing_education()

@router.get("/get_continuing_education_by_id/{id_continuing_education}")
async def get_continuing_education_by_id(id_continuing_education: int):    
    return new_continuing_education.get_continuing_education_by_id(id_continuing_education)

@router.put("/edit_continuing_education/{id_continuing_education}")
async def edit_continuing_education(id_continuing_education: int, continuing_education: continuing_education):    
    return new_continuing_education.edit_continuing_education(id_continuing_education, continuing_education)

@router.delete("/delete_continuing_education/{id_continuing_education}")
async def delete_continuing_education(id_continuing_education: int):    
    return new_continuing_education.delete_continuing_education(id_continuing_education)