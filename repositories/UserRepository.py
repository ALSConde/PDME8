from typing import List, Optional

from fastapi import Depends
from sqlalchemy.orm import Session, lazyload

from configs.Database import (
    get_db_connection,
)
from models.UserModel import User


class UserRepository:
    db: Session

    def __init__(
        self, db: Session = Depends(get_db_connection)
    ) -> None:
        self.db = db

    def list(
        self,
        name: Optional[str],
        limit: Optional[int],
        start: Optional[int],
    ) -> List[User]:
        query = self.db.query(User)

        if name:
            query = query.filter_by(name=name)

        return query.offset(start).limit(limit).all() # type: ignore

    def get_by_id(self, id: int) -> User:
        return self.db.query(User).get(id)

    def get_all(self) -> List[User]:
        return self.db.query(User).all()

    def create(self, user: User) -> User:
        print(f"chegou no Repository")
        print(user)
        self.db.add(user)
        print(f"falha no add")
        self.db.commit()
        self.db.refresh(user)
        return user

    def update(self, id: int, user: User) -> User:
        if not self.get_by_id(id):
            raise Exception("User not found")

        if user.id != id:
            raise Exception("User id does not match")

        self.db.merge(user)
        self.db.commit()

        return user

    def delete(self, user: User) -> None:
        self.db.delete(user)
        self.db.commit()
        self.db.flush()
