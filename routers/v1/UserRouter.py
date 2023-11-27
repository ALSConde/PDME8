from typing import List, Optional
from fastapi import APIRouter, Depends, status
from schemas.pydantic.UserSchema import (
    UserSchema,
    UserSchemaPostSchema,
)
from services.UserService import UserService

UserRouter = APIRouter(prefix="/v1/users", tags=["user"])


@UserRouter.get("/")
def get_index():
    return "Hello World"


@UserRouter.get("/list")
def list_users(
    name: Optional[str] = None,
    limit: Optional[int] = None,
    start: Optional[int] = None,
    userService: UserService = Depends(),
):
    return userService.list(name, limit, start)


@UserRouter.get("/{user_id}")
def get_user_by_id(user_id: int):
    return {}


@UserRouter.post(
    "/create/",
    response_model=UserSchema,
    status_code=status.HTTP_201_CREATED,
)
async def create_user(
    user: UserSchemaPostSchema,
    userService: UserService = Depends(),
):
    print(f"chegou no Router")
    return userService.create_user(user).normalize() # type: ignore
