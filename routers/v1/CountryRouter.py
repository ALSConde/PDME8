from fastapi import APIRouter
from schemas.pydantic.ApiResponse import ApiResponse

from schemas.pydantic.CountrySchema import CountrySchema


CountryRouter = APIRouter(
    prefix="/v1/countries", tags=["country"]
)


@CountryRouter.get(
    "/list"
)
async def list_countries():
    return {"message": "List of countries"}
