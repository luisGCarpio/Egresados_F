from pydantic import BaseModel
class employment_statuses(BaseModel):
    id_status: int = None
    description: str