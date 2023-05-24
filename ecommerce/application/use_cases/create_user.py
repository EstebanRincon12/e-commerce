# application/use_cases/create_user.py

from domain.models.User import User
from domain.repositories.UserRepository import UserRepository

class CreateUserUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, login: str, rol_name: str, id_person: int, password: str) -> User:
        # Realizar validaciones adicionales si es necesario

        user = User(login, rol_name, id_person, password)
        self.user_repository.create_user(user)

        return user
