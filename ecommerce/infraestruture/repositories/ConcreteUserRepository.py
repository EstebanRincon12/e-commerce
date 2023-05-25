from ecommerce.domain.repositories.UserRepository import UserRepository
from typing import Optional
from ecommerce.domain.models.User import User
from ecommerce.infraestruture.adapters.postgres_repository import PostgresUserRepository

class ConcreteUserRepository(UserRepository):

    def __init__(self):
        self.db = PostgresUserRepository()

    def create_user(self, user: User) -> None:
        # Lógica para crear un usuario en la persistencia
        self.db.create_user(user.login, user.rol_name, user.id_person, user.password)

    def get_user_by_id(self, user_id: int) -> Optional[User]:
        # Lógica para obtener un usuario por ID de la persistencia
        pass

    def get_user_by_login(self, login: str) -> Optional[User]:
        # Lógica para obtener un usuario por nombre de usuario de la persistencia
        pass

    def update_user(self, user: User) -> None:
        # Lógica para actualizar un usuario en la persistencia
        pass

    def delete_user(self, user_id: int) -> None:
        # Lógica para eliminar un usuario de la persistencia
        pass

    def authenticate_user(self, login: str, password: str) -> Optional[User]:
        # Lógica para autenticar un usuario en la persistencia
        pass
