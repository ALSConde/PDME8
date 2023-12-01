from pydantic import BaseModel


class CityPostSchema(BaseModel):
    name: str

    class Config:
        orm_mode = True


class CitySchema(CityPostSchema):
    id: int

    class Config:
        orm_mode = True
