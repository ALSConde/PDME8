from turtle import title
from typing import List, Optional
from fastapi import Depends
from sqlalchemy.orm import Session

from models.JobModel import Job
from repositories.JobRepository import JobRepository
from schemas.pydantic.JobSchema import JobSchema


class JobService:
    citiesRepo: JobRepository

    def __init__(
        self, citiesRepo: JobRepository = Depends()
    ):
        self.citiesRepo = citiesRepo

    def create_job(self, job_data: JobSchema):
        job = Job(
            title=job_data.title,
            description=job_data.description,
            salary=job_data.salary,
            company_id=job_data.company_id,
            new=job_data.new,
            remote=job_data.remote,
            fullTime=job_data.fullTime,
            partTime=job_data.partTime,
            featured=job_data.featured,
            skills_id=job_data.skills_id,
            active=job_data.active,
            categories=job_data.categories,
        )

        return self.citiesRepo.create(job)

    def update_job(self, job_id: int, job_data: JobSchema):
        job = Job(
            id=job_id,
            title=job_data.title,
            description=job_data.description,
            salary=job_data.salary,
            company_id=job_data.company_id,
            new=job_data.new,
            remote=job_data.remote,
            fullTime=job_data.fullTime,
            partTime=job_data.partTime,
            featured=job_data.featured,
            skills_id=job_data.skills_id,
            active=job_data.active,
            categories=job_data.categories,
        )

        return self.citiesRepo.update(job)

    def delete_job(self, job_id: int):
        job = self.citiesRepo.get_by_id(job_id)
        self.citiesRepo.delete(job)

    def get_job_by_id(self, job_id: int):
        return self.citiesRepo.get_by_id(job_id)

    def get_by_name(self, name: str):
        return self.citiesRepo.get_by_name(name)

    def list(
        self,
        name: Optional[str] = None,
        pageSize: Optional[int] = 100,
        startIndex: Optional[int] = 0,
    ) -> List[Job]:
        return self.citiesRepo.list(
            name, pageSize, startIndex
        )
