from pydantic import BaseModel

from schemas.pydantic.CitySchema import CitySchema


class LocationPostSchema(BaseModel):
    name: str
    city_id: int
    city: CitySchema | None = None
    address: str


class LocationSchema(LocationPostSchema):
    id: int
