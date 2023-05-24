# application/use_cases/authenticate_user.py

from ecommerce.domain.models.User import User
from ecommerce.domain.repositories.UserRepository import UserRepository

class AuthenticateUserUseCase:
    """ se utiliza para verificar las credenciales de un 
    usuario y determinar si son válidas.
    """
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, login: str, password: str) -> User:
        user = self.user_repository.get_user_by_login(login)
        if user and user.password == password:
            return user
        else:
            return None
