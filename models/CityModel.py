from sqlalchemy import Column, Integer, String
from models.BaseModel import BaseModel
from sqlalchemy.orm import relationship


class City(BaseModel):
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    state_id = Column(Integer, nullable=False)

    state = relationship(
        "state", backref="cities", lazy=True
    )

    def normalize(self):
        return {
            "id": self.id.__str__(),
            "name": self.name.__str__(),
            "state_id": self.state_id.__str__(),
        }
