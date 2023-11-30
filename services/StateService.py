from typing import List, Optional
from fastapi import Depends
from models.StateModel import State
from repositories.StateRepository import StateRepository
from schemas.pydantic.StateSchema import StateSchema


class StateService:
    statesRepo: StateRepository

    def __init__(
        self, statesRepo: StateRepository = Depends()
    ):
        self.statesRepo = statesRepo

    def create_state(self, state_data: StateSchema):
        state = State(
            name=state_data.name,
        )  # type: ignore

        return self.statesRepo.create(state)

    def update_state(
        self, state_id: int, state_data: StateSchema
    ):
        state = State(
            id=state_id,
            name=state_data.name,
            state_id=state_data,
        )  # type: ignore

        return self.statesRepo.update(state)

    def delete_city(self, state_id: int):
        state = self.statesRepo.get_by_id(state_id)
        self.statesRepo.delete(state)

    def get_state_by_id(self, state_id: int):
        return self.statesRepo.get_by_id(state_id)

    def get_by_name(self, name: str):
        return self.statesRepo.get_by_name(name)

    def list(
        self,
        name: Optional[str] = None,
        pageSize: Optional[int] = 100,
        startIndex: Optional[int] = 0,
    ) -> List[State]:
        return self.statesRepo.list(
            name, pageSize, startIndex
        )
