
import datetime
import secrets


class TokenValue:
    def __init__(self, valor, fecha_expiracion):
        self.valor = valor
        self.fecha_expiracion = fecha_expiracion

    def is_expired(self):
        return datetime.now() > self.fecha_expiracion

    def to_dict(self):
        return {
            "valor": self.valor,
            "fecha_expiracion": self.fecha_expiracion.isoformat(),
        }

    @staticmethod
    def from_dict(token_dict):
        return TokenValue(
            valor=token_dict["valor"],
            fecha_expiracion=datetime.fromisoformat(token_dict["fecha_expiracion"]),
        )

    @staticmethod
    def generate_random_token(length=32):
        random_bytes = secrets.token_bytes(length)
        token = secrets.token_urlsafe(length)[:length]
        return token