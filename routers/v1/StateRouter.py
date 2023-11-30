from fastapi import APIRouter

from schemas.pydantic.ApiResponse import ApiResponse
from schemas.pydantic.StateSchema import StateSchema


StateRouter = APIRouter(prefix="/v1/states", tags=["state"])


@StateRouter.get(
    "/list", response_model=ApiResponse[list[StateSchema]]
)
async def list_states():
    return {"message": "List of states"}
