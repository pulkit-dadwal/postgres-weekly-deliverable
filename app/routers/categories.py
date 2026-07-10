from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.category import Category
from app.schemas.category import CategoryCreate, CategoryResponse

router = APIRouter(prefix="/categories", tags=["Categories"])


@router.get("/")
def get_categories(db: Session = Depends(get_db)) -> list[CategoryResponse]:
    return db.query(Category).all()


@router.post("/")
def create_category(db: Session = Depends(get_db), category_data: CategoryCreate = None) -> CategoryResponse:
    category = Category(name=category_data.name)

    db.add(category)
    db.commit()
    db.refresh(category)

    return category