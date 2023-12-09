from turtle import title
from typing import List, Optional
from fastapi import Depends
from sqlalchemy.orm import Session

from models.CompanyModel import Company
from repositories.CompanyRepository import CompanyRepository
from schemas.pydantic.CompanySchema import CompanySchema


class CompanyService:
    citiesRepo: CompanyRepository

    def __init__(
        self, citiesRepo: CompanyRepository = Depends()
    ):
        self.citiesRepo = citiesRepo

    def create_company(self, company_data: CompanySchema):
        company = Company(
            name=company_data.name,
            website=company_data.website,
            email=company_data.email,
            description=company_data.description,
            active=company_data.active,
        )

        return self.citiesRepo.create(company)

    def update_company(
        self, company_id: int, company_data: CompanySchema
    ):
        company = Company(
            id=company_id,
            name=company_data.name,
            website=company_data.website,
            email=company_data.email,
            description=company_data.description,
            active=company_data.active,
        )

        return self.citiesRepo.update(company)

    def delete_company(self, company_id: int):
        company = self.citiesRepo.get_by_id(company_id)
        self.citiesRepo.delete(company)

    def get_company_by_id(self, company_id: int):
        return self.citiesRepo.get_by_id(company_id)

    def get_by_name(self, name: str):
        return self.citiesRepo.get_by_name(name)

    def list(
        self,
        name: Optional[str] = None,
        pageSize: Optional[int] = 100,
        startIndex: Optional[int] = 0,
    ) -> List[Company]:
        return self.citiesRepo.list(
            name, pageSize, startIndex
        )
