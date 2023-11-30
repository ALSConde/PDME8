from pydantic import BaseModel


class CityPostSchema(BaseModel):
    name: str
    state: str


class CitySchema(CityPostSchema):
    id: int
