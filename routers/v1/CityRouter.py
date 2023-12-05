from typing import Optional
from fastapi import APIRouter, Depends, status
from schemas.pydantic.ApiResponse import ApiResponse

from schemas.pydantic.Schemas import (
    CityPostSchema,
    CitySchema,
)

from services.CityService import CityService


CityRouter = APIRouter(prefix="/v1/cities", tags=["city"])


@CityRouter.get(
    "/list",
    response_model=ApiResponse[list[CitySchema]],
)
async def list_cities(
    name: Optional[str] = None,
    limit: Optional[int] = None,
    start: Optional[int] = None,
    cityService: CityService = Depends(),
):
    body: dict | CitySchema
    message: str

    if cityService.list(name, limit, start):
        body = cityService.list(name, limit, start)  # type: ignore
        message = "List of cities"
        return ApiResponse[list[CitySchema]](
            body=body,  # type: ignore
            message=message,
            status_code=status.HTTP_200_OK,
        )


@CityRouter.post(
    "/create", response_model=ApiResponse[CitySchema]
)
async def create_city(
    city_data: CityPostSchema,
    cityService: CityService = Depends(),
):
    body: dict | CitySchema
    message: str

    body = cityService.get_by_name(city_data.name)  # type: ignore

    if body:
        message = "City already exists"
        return ApiResponse[CitySchema](
            body=body,  # type: ignore
            message=message,
            status_code=status.HTTP_400_BAD_REQUEST,
        )
    else:
        body = cityService.create_city(city_data)  # type: ignore
        message = "City created"
        return ApiResponse[CitySchema](
            body=body,  # type: ignore
            message=message,
            status_code=status.HTTP_201_CREATED,
        )
