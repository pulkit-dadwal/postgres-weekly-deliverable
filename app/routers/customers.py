from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.customer import Customer
from app.schemas.customer import CustomerCreate, CustomerResponse

router = APIRouter(prefix="/customers", tags=["Customers"])


@router.get("/")
def get_customers(db: Session = Depends(get_db)) -> list[CustomerResponse]:
    return db.query(Customer).all()


@router.get("/{customer_id}")
def get_customer(customer_id: int, db: Session = Depends(get_db)) -> CustomerResponse | None:
    return db.query(Customer).filter(Customer.id == customer_id).first()


@router.post("/")
def create_customer(db: Session = Depends(get_db), customer_data: CustomerCreate = None) -> CustomerResponse:  
    customer = Customer(
        name=customer_data.name,
        email=customer_data.email,
        phone=customer_data.phone,
    )

    db.add(customer)
    db.commit()
    db.refresh(customer)

    return customer