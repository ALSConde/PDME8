from models.BaseModel import BaseModel
from sqlalchemy import Column, Integer, String


class JobApplicationStatus(BaseModel):
    __tablename__ = "job_application_statuses"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
