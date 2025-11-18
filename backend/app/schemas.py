from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ReviewCreate(BaseModel):
    contact_number: str
    user_name: Optional[str]
    product_name: Optional[str]
    product_review: Optional[str]

class ReviewOut(BaseModel):
    id: int
    contact_number: str
    user_name: Optional[str]
    product_name: Optional[str]
    product_review: Optional[str]
    created_at: datetime

    class Config:
        orm_mode = True
