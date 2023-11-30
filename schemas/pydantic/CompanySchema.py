from pydantic import BaseModel


class CompanyPostSchema(BaseModel):
    name: str
    website: str
    email: str
    description: str
    location: str | None = None
    active: bool


class CompanySchema(CompanyPostSchema):
    id: int