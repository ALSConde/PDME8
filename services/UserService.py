from typing import List, Optional
from fastapi import Depends
from models.UserModel import User

from repositories.UserRepository import UserRepository
from schemas.pydantic.UserSchema import UserSchema


class UserService:
    userRepository: UserRepository

    def __init__(
        self, userRepository: UserRepository = Depends()
    ) -> None:
        self.userRepository = userRepository

    def create_user(self, user_data: UserSchema):
        print(f"chegou no Service")
        return self.userRepository.create(
            User(
                name=user_data.name,
                email=user_data.email,
                phone=user_data.phone,
                profile=user_data.profile,
                experience=user_data.experience,
                password=user_data.password.__hash__(),
            ) # type: ignore
        )

    def update_user(self, user_id, user_data):
        if not self.userRepository.get_by_id(user_id):
            return None

        return self.userRepository.update(
            user_id, user_data
        )

    def delete_user(self, user_id):
        if not self.userRepository.get_by_id(user_id):
            return None
        return self.userRepository.delete(user_id)

    def get_user_by_id(self, user_id):
        return self.userRepository.get_by_id(user_id)

    def list(
        self,
        name: Optional[str] = None,
        pageSize: Optional[int] = 100,
        startIndex: Optional[int] = 0,
    ) -> List[User]:
        return self.userRepository.list(
            name, pageSize, startIndex
        )
