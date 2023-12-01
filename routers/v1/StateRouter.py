from typing import Optional
from fastapi import APIRouter, Depends, status

from schemas.pydantic.ApiResponse import ApiResponse
from schemas.pydantic.CityStateSchema import StateCitySchema
from schemas.pydantic.StateSchema import StateSchema
from services.StateService import StateService


StateRouter = APIRouter(prefix="/v1/states", tags=["state"])


@StateRouter.get(
    "/list", response_model=ApiResponse[list[StateSchema]]
)
async def list_states(
    name: Optional[str] = None,
    limit: Optional[int] = None,
    start: Optional[int] = None,
    stateService: StateService = Depends(),
):
    body: dict | StateSchema
    message: str

    if stateService.list(name, limit, start):
        body = userService.list(name, limit, start)  # type: ignore
        message = "List of users"
        return ApiResponse[list[StateCitySchema]](
            body=body,  # type: ignore
            message=message,
            status_code=status.HTTP_200_OK,
        )