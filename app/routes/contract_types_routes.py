from fastapi import APIRouter, HTTPException
from controllers.contract_types_controller import *

from models.contract_types_model import contract_types

router = APIRouter()

new_contract_type = contract_types_controller()

@router.post("/create_contract_type")
async def create_contract_type(contract_type: contract_types):
    return new_contract_type.create_contract_type(contract_type)

@router.get("/get_contract_types")
async def get_contract_types():
    return new_contract_type.get_contract_types()

@router.get("/get_contract_type/{id_contract_type}")
async def get_contract_type(id_contract_type:int):
    return new_contract_type.get_contract_type(id_contract_type)

@router.put("/edit_contract_type/{contract_type_id}")
async def edit_contract_type(contract_type_id:int,contract_type:contract_types):
    return new_contract_type.edit_contract_type(contract_type_id,contract_type)

@router.delete("/delete_contract_type/{id_contract_type}")
async def delete_contract_type(id_contract_type:int):
    return new_contract_type.delete_contract_type(id_contract_type)