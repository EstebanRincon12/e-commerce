import hashlib

class EncryptedPassword:
    """
    Clase que representa una contraseña encriptada.
    """

    def __init__(self, password):
        """
        Constructor de la clase EncryptedPassword.

        Args:
            password (str): Contraseña en texto plano.
        """
        self._hash = self._encrypt_password(password)


    @staticmethod
    def _encrypt_password(password):
        """
        Método estático que encripta una contraseña.

        Args:
            password (str): Contraseña en texto plano.

        Returns:
            str: Contraseña encriptada.
        """
        hash_object = hashlib.sha256(password.encode())
        hashed_password = hash_object.hexdigest()

        # Truncar el hash a la longitud deseada
        truncated_hash = hashed_password[:20]
        print(truncated_hash)
        return truncated_hash


    def verify_password(self, password):
        """
        Verifica si una contraseña coincide con la contraseña encriptada.

        Args:
            password (str): Contraseña en texto plano.

        Returns:
            bool: True si la contraseña coincide, False en caso contrario.
        """
        return self._hash == self._encrypt_password(password)
    

pal = EncryptedPassword('password')
