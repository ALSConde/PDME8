from models.BaseModel import BaseModel
from sqlalchemy import Column, Integer, String, Numeric, Boolean

from models.CompanyModel import Company
from models.JobCategoryModel import JobCategory
from models.SkillsModel import Skills


class Job(BaseModel):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False) 
    description = Column(String(4096), nullable=False)
    salary = Column(Numeric(10), nullable=False)
    company = Company()
    new = Column(Boolean, nullable=False, default=False)
    remote = Column(Boolean, nullable=False, default=False)
    fullTime = Column(Boolean, nullable=False, default=False)
    partTime = Column(Boolean, nullable=False, default=False)
    featured = Column(Boolean, nullable=False, default=False)
    skills = Skills[] # type: ignore
    active = Column(Boolean, nullable=False)
    categories = JobCategory[] # type: ignore

