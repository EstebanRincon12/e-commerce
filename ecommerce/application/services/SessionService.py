from datetime import datetime, timedelta
import jwt
from typing import Optional

from ecommerce.domain.models.User import User
from ecommerce.domain.repositories.UserRepository import UserRepository


class SessionService:
    def __init__(self):
        self.secret_key = "secret_key"
        self.expiration_time = 60

    def generate_token(self, user: User) -> str:
        """Genera un token JWT utilizando la 
        biblioteca jwt. Recibe como parámetro el ID 
        del usuario (user_id). Crea un payload que 
        incluye el ID del usuario y la fecha de 
        expiración del token. Luego, codifica el 
        payload utilizando la clave secreta y el 
        algoritmo HS256, y devuelve el token generado.

        Args:
            user_id (int): id_user

        Returns:
            str:  token generado
        """
        payload = {
            'user_id': user.id_person,
            'login': user.login,
            'role': user.rol_name._role,
            'exp': datetime.utcnow() + timedelta(minutes=self.expiration_time)
        }
        
        token = jwt.encode(payload, self.secret_key, algorithm='HS256')
        return token

    def validate_token(self, token: str) -> Optional[int]:
        """alida un token JWT. Recibe como parámetro el 
        token a validar. Utiliza la biblioteca jwt para 
        decodificar el token utilizando la clave 
        secreta y el algoritmo HS256. Si el token 
        está vigente y no ha expirado, extrae el ID 
        del usuario del payload y lo devuelve. En 
        caso de que el token haya expirado o sea 
        inválido, devuelve None.

        Args:
            token (str): token a validar

        Returns:
            Optional[int]: id del usuario 
        """
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=['HS256'])
            user_id = payload.get('user_id')
            return user_id
        except jwt.ExpiredSignatureError:
            return None
        except jwt.InvalidTokenError:
            return None


class AuthenticateUserUseCase:
    def __init__(self, user_repository: UserRepository, session_service: SessionService):
        self.user_repository = user_repository
        self.session_service = session_service

    def execute(self, login: str, password: str) -> str:
        user = self.user_repository.authenticate_user(login, password)
        if user:
            token = self.session_service.generate_token(user.id_person)
            return token
        else:
            raise Exception('Invalid credentials')
