import unittest
from unittest.mock import Mock
from ecommerce.application.use_cases.authenticate_user import AuthenticateUserUseCase
from ecommerce.domain.models.User import User
from ecommerce.domain.repositories.UserRepository import UserRepository

class AuthenticateUserUseCaseTest(unittest.TestCase):
    def test_execute_with_valid_credentials(self):
        # Arrange
        mock_user_repository = Mock(UserRepository)
        user = User(login='john', password='password')
        mock_user_repository.get_user_by_login.return_value = user
        use_case = AuthenticateUserUseCase(mock_user_repository)
        expected_user = user

        # Act
        actual_user = use_case.execute(login='john', password='password')

        # Assert
        self.assertEqual(expected_user, actual_user)

    def test_execute_with_valid_credentials(self):
    # Arrange
        mock_user_repository = Mock(UserRepository)
        user = User(login='john', rol_name='admin', id_person=1, password='password')
        mock_user_repository.get_user_by_login.return_value = user
        use_case = AuthenticateUserUseCase(mock_user_repository)
        expected_user = user

        # Act
        actual_user = use_case.execute(login='john', password='password')

        # Assert
        self.assertEqual(expected_user, actual_user)


if __name__ == '__main__':
    unittest.main()
