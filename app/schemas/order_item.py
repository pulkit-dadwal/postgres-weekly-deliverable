from pydantic import BaseModel


class OrderItemCreate(BaseModel):
    order_id: int
    product_id: int
    quantity: int


class OrderItemUpdate(BaseModel):
    quantity: int | None = None


class OrderItemResponse(BaseModel):
    id: int
    order_id: int
    product_id: int
    quantity: int

    model_config = {
        "from_attributes": True
    }