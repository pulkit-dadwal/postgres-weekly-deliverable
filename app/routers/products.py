from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.product import Product
from app.schemas.product import ProductCreate, ProductResponse

router = APIRouter(prefix="/products", tags=["Products"])


@router.get("/")
def get_products(db: Session = Depends(get_db)) -> list[ProductResponse]:
    return db.query(Product).all()


@router.post("/")
def create_product(db: Session = Depends(get_db), product_data: ProductCreate = None) -> ProductResponse:
    product = Product(
        name=product_data.name,
        price=product_data.price,
        category_id=product_data.category_id,
    )

    db.add(product)
    db.commit()
    db.refresh(product)

    return product