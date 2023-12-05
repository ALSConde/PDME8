from pydantic import BaseModel

from schemas.pydantic.CitySchema import CitySchema


class StatePostSchema(BaseModel):
    name: str
    initials: str
    country_id: int

    class Config:
        orm_mode = True


class StateSchema(StatePostSchema):
    id: int

    class Config:
        orm_mode = True
