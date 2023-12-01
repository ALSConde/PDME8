from models.BaseModel import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel):
    __tablename__ = "states"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    initials = Column(String(50), nullable=False)
    # city_id = Column(
    #     Integer, ForeignKey("cities.id"), nullable=False
    # )
    country_id = Column(Integer, nullable=False)
    cities = relationship(
        "City",
        back_populates="state",
    )

    def normalize(self):
        return {
            "id": self.id.__str__(),
            "name": self.name.__str__(),
            "initials": self.initials.__str__(),
            "country_id": self.country_id.__str__(),
        }
