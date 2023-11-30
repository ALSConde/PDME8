from models.BaseModel import BaseModel
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship
from models.LocationModel import Location


class Company(BaseModel):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    website = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    description = Column(String(50), nullable=False)
    location = relationship("Location", lazy=True, secondary="company_location")
    # location = Location()
    active = Column(Boolean, nullable=False)

    def normalize(self):
        return {
            "id": self.id.__str__(),
            "name": self.name.__str__(),
            "website": self.website.__str__(),
            "email": self.email.__str__(),
            "description": self.description.__str__(),
            "location": self.location.__str__(),
            "active": self.active.__str__(),
        }