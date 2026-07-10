from fastapi import FastAPI

from app.database import Base, engine

from app.routers import (
    customers,
    employees,
    categories,
    products,
    orders,
    order_items,
)

# Import every model so SQLAlchemy registers them
from app.models.customer import Customer
from app.models.employee import Employee
from app.models.category import Category
from app.models.product import Product
from app.models.order import Order
from app.models.order_item import OrderItem

app = FastAPI(title="Coffee Shop Management API")

Base.metadata.create_all(bind=engine)

app.include_router(customers.router)
app.include_router(employees.router)
app.include_router(categories.router)
app.include_router(products.router)
app.include_router(orders.router)
app.include_router(order_items.router)


@app.get("/")
def home():
    return {"message": "Coffee Shop Management API is running!"}