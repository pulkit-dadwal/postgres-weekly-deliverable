from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.order_item import OrderItem
from app.schemas.order_item import OrderItemCreate, OrderItemResponse

router = APIRouter(prefix="/order-items", tags=["Order Items"])


@router.get("/")
def get_order_items(db: Session = Depends(get_db)) -> list[OrderItemResponse]:
    return db.query(OrderItem).all()


@router.post("/")
def create_order_item(db: Session = Depends(get_db), order_item_data: OrderItemCreate = None) -> OrderItemResponse:
    item = OrderItem(
        order_id=order_item_data.order_id,
        product_id=order_item_data.product_id,
        quantity=order_item_data.quantity,
    )

    db.add(item)
    db.commit()
    db.refresh(item)

    return item