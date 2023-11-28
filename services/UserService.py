from typing import List, Optional
from fastapi import Depends
from models.UserModel import User

from repositories.UserRepository import UserRepository
from schemas.pydantic.UserSchema import (
    UserPostSchema,
    UserSchema,
)


class UserService:
    userRepository: UserRepository

    def __init__(
        self, userRepository: UserRepository = Depends()
    ) -> None:
        self.userRepository = userRepository

    def create_user(self, user_data: UserSchema):
        return self.userRepository.create(
            User(
                name=user_data.name,
                email=user_data.email,
                phone=user_data.phone,
                profile=user_data.profile,
                experience=user_data.experience,
                password=user_data.password.__hash__(),
            )  # type: ignore
        )

    def update_user(
        self, user_id: int, user_data: UserPostSchema
    ):
        return self.userRepository.update(
            user=User(
                id=user_id,
                name=user_data.name,
                email=user_data.email,
                phone=user_data.phone,
                profile=user_data.profile,
                experience=user_data.experience,
                password=user_data.password,
            ), # type: ignore
        )

    def delete_user(self, user_id):
        if not self.userRepository.get_by_id(user_id):
            return None
        return self.userRepository.delete(user_id)

    def get_user_by_id(self, user_id):
        return self.userRepository.get_by_id(user_id)

    def get_user_by_email(self, email):
        if email is None:
            return {}

        if email == "" or email == " ":
            return {}

        return self.userRepository.get_by_email(email)

    def list(
        self,
        name: Optional[str] = None,
        pageSize: Optional[int] = 100,
        startIndex: Optional[int] = 0,
    ) -> List[User]:
        return self.userRepository.list(
            name, pageSize, startIndex
        )
