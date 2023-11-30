from models.BaseModel import BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class State(BaseModel):
    __tablename__ = "states"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    initials = Column(String(50), nullable=False)
    country_id = Column(Integer, nullable=False)

    country = relationship(
        "country", backref="states", lazy=True
    )

    cities = relationship(
        "cities", backref="states", lazy=True
    )

    def normalize(self):
        return {
            "id": self.id.__str__(),
            "name": self.name.__str__(),
            "initials": self.initials.__str__(),
            "country_id": self.country_id.__str__(),
        }
