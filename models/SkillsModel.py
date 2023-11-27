from models.BaseModel import BaseModel
from sqlalchemy import Column, Integer, String


class Skills(BaseModel):
    __tablename__ = "skills"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
