from pydantic import BaseModel

from schemas.pydantic.CitySchema import CitySchema


class StatePostSchema(BaseModel):
    name: str
    initials: str
    coutry: str
    cities: CitySchema | None = None


class StateSchema(StatePostSchema):
    id: int
