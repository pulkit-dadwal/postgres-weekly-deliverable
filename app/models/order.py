from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey, String
from datetime import datetime
from app.database import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)

    customer_id = Column(Integer, ForeignKey("customers.id"))

    employee_id = Column(Integer, ForeignKey("employees.id"))

    total_amount = Column(Float)

    order_time = Column(DateTime, default=datetime.utcnow)

    status = Column(String)