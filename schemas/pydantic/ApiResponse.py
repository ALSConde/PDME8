from typing import Generic, TypeVar
from pydantic import BaseModel


T = TypeVar("T")


class ApiResponse(Generic[T], BaseModel):
    message: str
    status_code: int
    body: T | dict = {}
