from ecommerce.domain.value_objects.EncryptedPassword import EncryptedPassword
from ecommerce.domain.value_objects.UserRole import UserRole


class User:
    """
    Clase que representa a un usuario en el sistema.
    """

    def __init__(self, login, rol_name, id_person, password):
        """
        Constructor de la clase User.

        Args:
            login (str): Nombre de usuario.
            rol_name (str): Nombre del rol del usuario.
            description (str): Descripción del usuario.
            id_person (int): Identificador único del usuario.
            password (str): Contraseña del usuario.
        """
        self._login = login
        self._rol_name = UserRole(rol_name)
        self._id_person = id_person
        self._password = EncryptedPassword(password)


    def serialize(self):
        return {
            'login': self.login,
            'rol_name': self.rol_name._role,
            'id_person': self.id_person,
            'password': self.password._hash
        }

    @property
    def login(self):
        """
        Propiedad que devuelve el nombre de usuario.

        Returns:
            str: Nombre de usuario.
        """
        return self._login

    @property
    def rol_name(self):
        """
        Propiedad que devuelve el nombre del rol del usuario.

        Returns:
            str: Nombre del rol del usuario.
        """
        return self._rol_name

    @property
    def id_person(self):
        """
        Propiedad que devuelve el identificador único del usuario.

        Returns:
            int: Identificador único del usuario.
        """
        return self._id_person

    @property
    def password(self):
        """
        Propiedad que devuelve la contraseña del usuario.

        Returns:
            str: Contraseña del usuario.
        """
        return self._password
    
    def verify_password(self, password):
        return self._password.verify_password(password)
