from pydantic import BaseModel


class CountryPostSchema(BaseModel):
    name: str
    initials: str


class CountrySchema(CountryPostSchema):
    id: int
