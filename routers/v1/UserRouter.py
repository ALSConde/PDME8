from typing import Optional
from fastapi import APIRouter, Depends, Response, status
from schemas.pydantic.ApiResponse import ApiResponse
from schemas.pydantic.UserSchema import (
    UserSchema,
    UserPostSchema,
)
from services.UserService import UserService

UserRouter = APIRouter(prefix="/v1/users", tags=["user"])


@UserRouter.get("/")
def get_index():
    return "Hello World"


@UserRouter.get(
    "/list", response_model=ApiResponse[list[UserSchema]]
)
async def list_users(
    name: Optional[str] = None,
    limit: Optional[int] = None,
    start: Optional[int] = None,
    userService: UserService = Depends(),
):
    body: dict | UserSchema
    message: str

    if userService.list(name, limit, start):
        body = userService.list(name, limit, start)  # type: ignore
        message = "List of users"
        return ApiResponse[list[UserSchema]](
            body=body,  # type: ignore
            message=message,
            status_code=status.HTTP_200_OK,
        )


@UserRouter.get("/{user_id}", response_model=ApiResponse[UserSchema])
def get_user_by_id(
    user_id: int, userService: UserService = Depends()
):
    body: dict | UserSchema
    message: str

    if userService.get_user_by_id(user_id):
        body = userService.get_user_by_id(
            user_id
        ).normalize()
        message = "User found"
        return ApiResponse[UserSchema](
            body=body,
            message=message,
            status_code=status.HTTP_200_OK,
        )
    else:
        message = "User not found"
        return ApiResponse[UserSchema](
            message=message,
            status_code=status.HTTP_404_NOT_FOUND,
        )


@UserRouter.post(
    "/create/",
    response_model=ApiResponse[UserSchema],
    status_code=status.HTTP_201_CREATED,
)
async def create_user(
    user: UserPostSchema,
    res: Response,
    userService: UserService = Depends(),
):
    body: dict | UserSchema
    message: str

    if userService.get_user_by_email(user.email):
        res.status_code = status.HTTP_409_CONFLICT
        message = "Email already exists"
        return ApiResponse[UserSchema](
            message=message,
            status_code=res.status_code,
        )
    else:
        res.status_code = status.HTTP_201_CREATED
        message = "User created successfully"
        body = userService.create_user(user).normalize()  # type: ignore
        return ApiResponse[UserSchema](
            body=body,
            message=message,
            status_code=res.status_code,
        )
