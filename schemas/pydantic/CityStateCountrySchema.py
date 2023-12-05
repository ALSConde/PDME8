from schemas.pydantic.CountrySchema import CountrySchema
from .CitySchema import CitySchema
from .StateSchema import StateSchema


class CityStateSchema(CitySchema):
    state: StateSchema

    class Config:
        orm_mode = True


class StateCitySchema(StateSchema):
    cities: list[CitySchema]

    class Config:
        orm_mode = True


class StateCountrySchema(StateSchema):
    country: CountrySchema

    class Config:
        orm_mode = True


class CountryStatesSchema(CountrySchema):
    states: list[StateSchema]

    class Config:
        orm_mode = True
