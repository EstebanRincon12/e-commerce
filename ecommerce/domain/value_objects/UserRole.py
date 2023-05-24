class UserRole:
    """
    Clase que representa el rol de un usuario.
    """

    VALID_ROLES = ['admin', 'user']

    def __init__(self, role):
        """
        Constructor de la clase UserRole.

        Args:
            role (str): Rol del usuario.
        """
        self._role = self._validate_role(role)

    @staticmethod
    def _validate_role(role):
        """
        Método estático que valida el rol del usuario.

        Args:
            role (str): Rol del usuario.

        Returns:
            str: Rol validado.

        Raises:
            ValueError: Si el rol no es válido.
        """
        if role.lower() not in UserRole.VALID_ROLES:
            raise ValueError("Rol inválido")
        return role.lower()

    @property
    def role(self):
        """
        Propiedad que devuelve el rol del usuario.

        Returns:
            str: Rol del usuario.
        """
        return self._role