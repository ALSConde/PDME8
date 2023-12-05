from pydantic import BaseModel


class UserPostSchema(BaseModel):
    name: str
    email: str
    phone: str
    profile: str | None
    experience: str | None
    password: str

    class Config:
        orm_mode = True


class UserSchema(UserPostSchema):
    id: int

    class Config:
        orm_mode = True

    from pydantic import BaseModel


class CityPostSchema(BaseModel):
    name: str
    state_id: int

    class Config:
        orm_mode = True


class CitySchema(CityPostSchema):
    id: int

    class Config:
        orm_mode = True


class StatePostSchema(BaseModel):
    name: str
    initials: str
    cities: list[CitySchema] = []
    country: "CountrySchema"

    class Config:
        orm_mode = True


class StateSchema(StatePostSchema):
    id: int

    class Config:
        orm_mode = True


class CountryPostSchema(BaseModel):
    name: str
    initials: str
    states: list[StateSchema] = []

    class Config:
        orm_mode = True


class CountrySchema(CountryPostSchema):
    id: int

    class Config:
        orm_mode = True
