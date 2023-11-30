from pydantic import BaseModel


class LocationPostSchema(BaseModel):
    name: str
    city: str | None = None
    address: str


class LocationSchema(LocationPostSchema):
    id: int
