from pydantic import BaseModel


class UserSchemaPostSchema(BaseModel):
    name: str
    email: str
    phone: str
    profile: str | None
    experience: str | None
    password: str 


class UserSchema(UserSchemaPostSchema):
    id: int
