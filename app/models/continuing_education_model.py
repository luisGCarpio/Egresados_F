from pydantic import BaseModel
from datetime import date
class continuing_education(BaseModel):
    id_continuing_education: int = None
    id_graduate: int
    description_program: str
    education_type: str
    time: str
    education_date: date