from datetime import datetime, timedelta
import jwt

class SessionService:
    def __init__(self, secret_key: str, expiration_time: int):
        self.secret_key = secret_key
        self.expiration_time = expiration_time

    def generate_token(self, user_id: int) -> str:
        payload = {
            'user_id': user_id,
            'exp': datetime.utcnow() + timedelta(minutes=self.expiration_time)
        }
        
        token = jwt.encode(payload, self.secret_key, algorithm='HS256')
        return token

    def validate_token(self, token: str) -> Optional[int]:
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=['HS256'])
            user_id = payload.get('user_id')
            return user_id
        except jwt.ExpiredSignatureError:
            return None
        except jwt.InvalidTokenError:
            return None
