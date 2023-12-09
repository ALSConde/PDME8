from typing import Optional
from fastapi import APIRouter, Depends, status
from schemas.pydantic.ApiResponse import ApiResponse

from schemas.pydantic.JobSchema import (
    JobSchema,
    JobSchemaPost,
)
