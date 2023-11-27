from BaseModel import BaseModel, EntityMeta
from sqlalchemy import Column, Integer, String, Boolean, Table, ForeignKey

company_location = Table(
    "company_location",
    EntityMeta.metadata,
    Column(
        "company_id", Integer, ForeignKey("companies.id")
    ),
    Column(
        "location_id", Integer, ForeignKey("locations.id")
    ),
)
