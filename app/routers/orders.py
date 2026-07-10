from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.order import Order
from app.schemas.order import OrderCreate, OrderResponse

router = APIRouter(prefix="/orders", tags=["Orders"])


@router.get("/")
def get_orders(db: Session = Depends(get_db)) -> list[OrderResponse]:
    return db.query(Order).all()


@router.post("/")
def create_order(db: Session = Depends(get_db), order_data: OrderCreate = None) -> OrderResponse:
    order = Order(
        customer_id=order_data.customer_id,
        employee_id=order_data.employee_id,
        total_amount=order_data.total_amount,
        status=order_data.status,
    )

    db.add(order)
    db.commit()
    db.refresh(order)

    return order