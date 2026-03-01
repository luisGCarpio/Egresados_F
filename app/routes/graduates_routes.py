from fastapi import APIRouter, HTTPException
from controllers.graduates_controller import *

from models.graduates_model import graduates

router = APIRouter()

new_graduates = graduates_controller()

@router.post("/create_graduates")
async def create_graduates(graduates: graduates):    
    return new_graduates.create_graduates(graduates)

@router.get("/get_graduates")
async def get_graduates():    
    return new_graduates.get_graduates()    

@router.get("/get_graduates/{id_graduate}")
async def get_graduate(id_graduate: int):    
    return new_graduates.get_graduate(id_graduate)    

@router.put("/edit_graduates/{id_graduate}")
async def edit_graduate(id_graduate: int, graduates: graduates):    
    return new_graduates.edit_graduate(graduates, id_graduate)    

@router.delete("/delete_graduates/{id_graduate}")
async def delete_graduate(id_graduate: int):    
    return new_graduates.delete_graduate(id_graduate)