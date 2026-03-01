from pydantic import BaseModel
class work_supervisor(BaseModel):
    id_supervisor: int = None
    id_program: int
    nombre_profesor: str
    id_graduate: int
    first_name: str
    id_job: int