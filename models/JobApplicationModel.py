from models.BaseModel import BaseModel
from sqlalchemy import Column, Integer, String


class JobApplication(BaseModel):
    __tablename__ = "job_applications"

    id = Column(Integer, primary_key=True)
    job_id = Column(Integer, nullable=False)
    user_id = Column(Integer, nullable=False)
    status = Column(String(50), nullable=False)
