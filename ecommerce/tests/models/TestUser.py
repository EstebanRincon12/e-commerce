import unittest
from ecommerce.domain.models.User  import User

class UserTestCase(unittest.TestCase):
    def setUp(self):
        self.user = User("john_doe", "admin", 1, "password123")

    def test_login(self):
        self.assertEqual(self.user.login, "john_doe")

    def test_rol_name(self):
        self.assertEqual(self.user.rol_name, "admin")

    def test_id_person(self):
        self.assertEqual(self.user.id_person, 1)

    def test_password(self):
        self.assertEqual(self.user.password, "password123")

if __name__ == '__main__':
    unittest.main()