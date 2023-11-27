from models.BaseModel import BaseModel
from sqlalchemy import Column, Integer, String

class JobCategory(BaseModel):
    __tablename__ = "job_categories"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)