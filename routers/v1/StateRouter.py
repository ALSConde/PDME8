from typing import Optional
from fastapi import APIRouter, Depends, status
from models.StateModel import State

from schemas.pydantic.ApiResponse import ApiResponse
from schemas.pydantic.Schemas import (
    StateSchema,
    StatePostSchema,
)
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
        body = stateService.list(name, limit, start)  # type: ignore
        message = "List of States"
        return ApiResponse[list[StateSchema]](
            body=body,  # type: ignore
            message=message,
            status_code=status.HTTP_200_OK,
        )


@StateRouter.post(
    "/create", response_model=ApiResponse[StateSchema]
)
async def create_state(
    state_data: StatePostSchema,
    stateService: StateService = Depends(),
):
    body: dict | StateSchema
    message: str

    if stateService.create_state(state_data=state_data):
        body = stateService.create_state(state_data=state_data)  # type: ignore
        message = "State created successfully"
        return ApiResponse[StateSchema](
            body=body,  # type: ignore
            message=message,
            status_code=status.HTTP_201_CREATED,
        )
