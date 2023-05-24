from domain.repositories.UserRepository import UserRepository
from domain.models.User import User

class AuthenticationService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def authenticate(self, username: str, password: str):
        user = self.user_repository.get_user_by_username(username)
        if user and user.password == password:
            return user
        else:
            return None

class UserCreationService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def create_user(self, username: str, password: str, role: str, email: str):
        user = User(username, password, role, email)
        self.user_repository.save_user(user)
        return user
