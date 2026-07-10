from pydantic import BaseModel
from datetime import datetime


class OrderCreate(BaseModel):
    customer_id: int
    employee_id: int
    total_amount: float
    status: str


class OrderUpdate(BaseModel):
    total_amount: float | None = None
    status: str | None = None


class OrderResponse(BaseModel):
    id: int
    customer_id: int
    employee_id: int
    total_amount: float
    status: str
    order_time: datetime

    model_config = {
        "from_attributes": True
    }