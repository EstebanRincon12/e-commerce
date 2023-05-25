import unittest
from unittest.mock import Mock
from ecommerce.domain.repositories.UserRepository import UserRepository
from ecommerce.domain.models.User import User
from ecommerce.application.use_cases.create_user import CreateUserUseCase

class UserCreationServiceTest(unittest.TestCase):

    def setUp(self):
        self.user_repository = Mock(spec=UserRepository)
        self.user_creation_service = CreateUserUseCase(self.user_repository)

    def test_create_user(self):
        # Datos de ejemplo para el nuevo usuario
        username = "john_doe"
        password = "password"
        role = "admin"
        email = "john.doe@example.com"

        # Simular el comportamiento del repositorio
        self.user_repository.create_user.return_value = None

        # Llamar al método del caso de uso
        result = self.user_creation_service.execute(username, role, 190909, password)

        # Verificar que el método del repositorio fue llamado con los parámetros correctos
        self.user_repository.create_user.assert_called_once()
        self.user_repository.create_user.assert_called_once_with(
            User(username, role, 190909, password)
        )

        # Verificar que se devolvió el objeto User esperado
        self.assertIsInstance(result, User)
        self.assertEqual(result.login, username)
        self.assertEqual(result.rol_name, role)
        self.assertEqual(result.id_person, 190909)
        self.assertEqual(result.password, password)

if __name__ == "__main__":
    unittest.main()
