from models.BaseModel import BaseModel
from sqlalchemy import Column, Integer, String, Numeric, Boolean

from models.CompanyModel import Company
from models.JobCategoryModel import JobCategory
from models.SkillsModel import Skills


class Job(BaseModel):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False) 
    description = Column(String(50), nullable=False)
    salary = Column(Numeric(5), nullable=False)
    company = Company()
    new = Column(Boolean, nullable=False)
    remote = Column(Boolean, nullable=False)
    time = Column(String(50), nullable=False)
    skills = Skills[] # type: ignore
    active = Column(Boolean, nullable=False)
    categories = JobCategory[] # type: ignore

