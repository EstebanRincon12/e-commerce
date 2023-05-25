from ecommerce.domain.repositories.UserRepository import UserRepository
from ecommerce.application.use_cases.create_user import CreateUserUseCase
from ecommerce.domain.models.User import User

class AuthenticationService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def authenticate(self, username: str, password: str):
        user = self.user_repository.get_user_by_username(username)
        if user and user.password == password:
            return user
        else:
            return None


class UserService:
    """actúa como una capa intermedia entre el controlador y los 
    casos de uso. Su responsabilidad principal es orquestar la 
    lógica de negocio y coordinar la interacción entre los casos 
    de uso y los adaptadores de repositorio.
    """
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository
        self.create_user_use_case = CreateUserUseCase(self.user_repository)

    def create_user(self, login: str, rol_name: str, id_person: int, password: str) -> User:
        return self.create_user_use_case.execute(login, rol_name, id_person, password)

