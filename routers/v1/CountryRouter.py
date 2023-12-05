from typing import Optional
from fastapi import APIRouter, Depends, status
from schemas.pydantic.ApiResponse import ApiResponse
from schemas.pydantic.Schemas import CountrySchema, CountryPostSchema
from services.CountryService import CountryService


CountryRouter = APIRouter(
    prefix="/v1/countries", tags=["country"]
)


@CountryRouter.get(
    "/list",
    response_model=ApiResponse[list[CountrySchema]]
)
async def list_countries(
    name: Optional[str] = None,
    limit: Optional[int] = None,
    start: Optional[int] = None,
    countryService: CountryService = Depends(),
):
    body: dict | CountrySchema
    message: str

    if countryService.list(name, limit, start):
        body = countryService.list(name, limit, start) # type: ignore
        message = "List of countries"
        return ApiResponse[list[CountrySchema]](
            body=body, # type: ignore
            message=message,
            status_code=status.HTTP_200_OK,
        )

