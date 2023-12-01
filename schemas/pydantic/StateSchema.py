from pydantic import BaseModel

from schemas.pydantic.CitySchema import CitySchema


class StatePostSchema(BaseModel):
    name: str
    initials: str


class StateSchema(StatePostSchema):
    id: int
