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
    address = Column(String(50), nullable=False)

    def normalize(self):
        return {
            "id": self.id.__str__(),
            "name": self.name.__str__(),
            "city": self.city.__str__(),
            "address": self.address.__str__(),
        }
