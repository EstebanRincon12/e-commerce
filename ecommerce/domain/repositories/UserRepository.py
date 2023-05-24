from abc import ABC, abstractmethod
from typing import Optional, List

from domain.models.User import User

class UserRepository(ABC):
    @abstractmethod
    def create_user(self, user: User) -> None:
        pass

    @abstractmethod
    def get_user_by_id(self, user_id: int) -> Optional[User]:
        pass

    @abstractmethod
    def get_user_by_login(self, login: str) -> Optional[User]:
        pass

    @abstractmethod
    def update_user(self, user: User) -> None:
        pass

    @abstractmethod
    def delete_user(self, user_id: int) -> None:
        pass

    @abstractmethod
    def authenticate_user(self, login: str, password: str) -> Optional[User]:
        pass
