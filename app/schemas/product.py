from pydantic import BaseModel


class ProductCreate(BaseModel):
    name: str
    price: float
    category_id: int


class ProductUpdate(BaseModel):
    name: str | None = None
    price: float | None = None
    category_id: int | None = None


class ProductResponse(BaseModel):
    id: int
    name: str
    price: float
    category_id: int

    model_config = {
        "from_attributes": True
    }