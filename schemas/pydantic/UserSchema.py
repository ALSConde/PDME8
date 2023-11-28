from pydantic import BaseModel


class UserPostSchema(BaseModel):
    name: str
    email: str
    phone: str
    profile: str | None
    experience: str | None
    password: str 


class UserSchema(UserPostSchema):
    id: int
