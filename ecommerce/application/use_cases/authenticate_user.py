# application/use_cases/authenticate_user.py

from domain.models.User import User
from domain.repositories.UserRepository import UserRepository

class AuthenticateUserUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, login: str, password: str) -> User:
        user = self.user_repository.get_user_by_login(login)
        if user and user.password == password:
            return user
        else:
            return None
