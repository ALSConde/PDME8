from models.BaseModel import BaseModel
from sqlalchemy import Column, Integer, String


class Skills(BaseModel):
    __tablename__ = "skills"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)

    def normalize(self):
        return {
            "id": self.id.__str__(),
            "name": self.name.__str__(),
        }