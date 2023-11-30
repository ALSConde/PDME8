from sqlalchemy import Column, Integer, String, ForeignKey
from models.BaseModel import BaseModel
from sqlalchemy.orm import relationship

class City(BaseModel):
    __tablename__ = "cities"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    state_id = Column(
        Integer, ForeignKey("states.id"), nullable=False
    )
    state = relationship("State", back_populates="state")

    def normalize(self):
        return {
            "id": self.id.__str__(),
            "name": self.name.__str__(),
            "state_id": self.state_id.__str__(),
        }
