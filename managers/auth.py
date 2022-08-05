from datetime import datetime, timedelta
from decouple import config

import jwt
from jwt import ExpiredSignatureError, InvalidTokenError
from werkzeug.exceptions import BadRequest


class AuthManager:
    @staticmethod
    def encode_token(user):
        payload = {"sub": user.email, "exp": datetime.utcnow() + timedelta(days=2)}
        return jwt.encode(payload, key=config("JWT_SECRET"), algorithm="HS256")

    @staticmethod
    def decode_token(token):
        # TODO fix errors
        try:
            payload = jwt.decode(token, key=config("JWT_SECRET"), algorithms=["HS256"])
            return payload["sub"]
        except ExpiredSignatureError:
            raise BadRequest("Token expired")
        except InvalidTokenError:
            raise BadRequest("Invalid token")

# auth = HTTPTokenAuth(scheme="Bearer")
