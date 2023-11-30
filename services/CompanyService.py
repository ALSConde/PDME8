from fastapi import Depends
from repositories.CompanyRepository import CompanyRepository


class CompanyService:
    companyRepo: CompanyRepository

    def __init__(
            self, companyRepo: CompanyRepository = Depends()
        ) -> None:
            self.companyRepo = companyRepo

    def create_company(self, user_data: UserSchema):
        hash_password = get_password_hash(
            user_data.password
        )

        user = User(
            name=user_data.name,
            email=user_data.email,
            phone=user_data.phone,
            profile=user_data.profile,
            experience=user_data.experience,
            password=hash_password,
        )  # type: ignore

        return self.userRepository.create(user=user)

    def update_user(
        self, user_id: int, user_data: UserPostSchema
    ):
        password = get_password_hash(user_data.password)

        user = User(
            id=user_id,
            name=user_data.name,
            email=user_data.email,
            phone=user_data.phone,
            profile=user_data.profile,
            experience=user_data.experience,
            password=password,
        )  # type: ignore

        return self.userRepository.update(user=user)

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