import unittest
from unittest.mock import MagicMock
from ecommerce.application.use_cases.create_user import CreateUserUseCase
from ecommerce.domain.models.User import User

class CreateUserUseCaseTests(unittest.TestCase):
    def test_create_user(self):
        # Simular el repositorio de usuarios
        user_repository = MagicMock()
        
        # Crear el caso de uso
        use_case = CreateUserUseCase(user_repository)

        # Datos de prueba
        login = "john.doe"
        rol_name = "admin"
        id_person = 1
        password = "password123"

        # Ejecutar el caso de uso
        result = use_case.execute(login, rol_name, id_person, password)

        # Verificar que el usuario haya sido creado
        self.assertIsInstance(result, User)
        self.assertEqual(result.login, login)
        self.assertEqual(result.rol_name, rol_name)
        self.assertEqual(result.id_person, id_person)
        self.assertEqual(result.password, password)

        # Verificar que el método `create_user` del repositorio haya sido llamado
        user_repository.create_user.assert_called_once_with(result)

if __name__ == '__main__':
    unittest.main()
