from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func
from .database import Base

class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
    contact_number = Column(String(50), nullable=False)
    user_name = Column(String(200), nullable=True)
    product_name = Column(String(200), nullable=True)
    product_review = Column(Text, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
