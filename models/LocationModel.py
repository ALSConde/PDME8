from models.CityModel import City
from models.BaseModel import BaseModel
from sqlalchemy import Column, Integer, String


class Location(BaseModel):
    __tablename__ = "locations"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    city = City()
    address = Column(String(50), nullable=False)
