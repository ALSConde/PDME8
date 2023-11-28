from models.CityModel import City
from models.BaseModel import BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class Location(BaseModel):
    __tablename__ = "locations"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    city = relationship(
        "City", lazy=True, secondary="city_location"
    )
    # city = City()
    address = Column(String(50), nullable=False)
