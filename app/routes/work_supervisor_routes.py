from fastapi import APIRouter, HTTPException    
from controllers.work_supervisor_controller import *
from models.work_supervisor_model import work_supervisor

router = APIRouter()

new_work_supervisor = work_supervisor_controller()

@router.post("/create_work_supervisor")
async def create_work_supervisor(work_supervisor: work_supervisor):
    return new_work_supervisor.create_work_supervisor(work_supervisor)

@router.get("/get_work_supervisors")
async def get_work_supervisors():
    return new_work_supervisor.get_work_supervisors()

@router.get("/get_work_supervisor/{id_supervisor}")
async def get_work_supervisor(id_supervisor: int):
    return new_work_supervisor.get_work_supervisor(id_supervisor)

@router.put("/edit_work_supervisor/{id_supervisor}")
async def edit_work_supervisor(id_supervisor: int, work_supervisor: work_supervisor):
    return new_work_supervisor.edit_work_supervisor(id_supervisor, work_supervisor)

@router.delete("/delete_work_supervisor/{id_supervisor}")
async def delete_work_supervisor(id_supervisor: int):
    return new_work_supervisor.delete_work_supervisor(id_supervisor)