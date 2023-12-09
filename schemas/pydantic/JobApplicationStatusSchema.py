from pydantic import BaseModel


class CompanyLocationSchemaPost(BaseModel):
    name: str

    class Config:
        from_attributes = True


class CompanyLocationSchema(CompanyLocationSchemaPost):
    id: int

    class Config:
        from_attributes = True
