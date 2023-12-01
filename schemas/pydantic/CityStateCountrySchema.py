from .CitySchema import CitySchema
from .StateSchema import StateSchema

class CityStateSchema(CitySchema):
    state: StateSchema

    class Config:
        orm_mode = True
    

class StateCitySchema:
    cities: list[CitySchema]

    class Config:
        orm_mode = True