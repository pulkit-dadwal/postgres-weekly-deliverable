
from pydantic import BaseModel


class EmployeeCreate(BaseModel):
    name: str
    role: str


class EmployeeUpdate(BaseModel):
    name: str | None = None
    role: str | None = None


class EmployeeResponse(BaseModel):
    id: int
    name: str
    role: str

    model_config = {
        "from_attributes": True
    }