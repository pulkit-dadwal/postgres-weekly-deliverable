from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.employee import Employee
from app.schemas.employee import EmployeeCreate, EmployeeResponse

router = APIRouter(prefix="/employees", tags=["Employees"])


@router.get("/")
def get_employees(db: Session = Depends(get_db)) -> list[EmployeeResponse]:
    return db.query(Employee).all()


@router.post("/")
def create_employee(db: Session = Depends(get_db), employee_data: EmployeeCreate = None) -> EmployeeResponse:
    employee = Employee(
        name=employee_data.name,
        role=employee_data.role,
    )

    db.add(employee)
    db.commit()
    db.refresh(employee)

    return employee