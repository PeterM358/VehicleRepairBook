from datetime import datetime, timedelta
from decouple import config

import jwt
from flask_httpauth import HTTPTokenAuth
from jwt import ExpiredSignatureError, InvalidTokenError
from werkzeug.exceptions import BadRequest, Unauthorized


class AuthManager:
    @staticmethod
    def encode_token(user):
        payload = {"sub": user.id, "exp": datetime.utcnow() + timedelta(days=2)}
        return jwt.encode(payload, key=config("JWT_SECRET"), algorithm="HS256")

    @staticmethod
    def decode_token(token):
        # TODO fix errors raises
        try:
            payload = jwt.decode(token, key=config("JWT_SECRET"), algorithms=["HS256"])
            return payload["sub"]
        except ExpiredSignatureError:
            raise BadRequest("Token expired")
        except InvalidTokenError:
            raise BadRequest("Invalid token")


auth = HTTPTokenAuth(scheme="Bearer")


@auth.verify_token
def verify_token(token):
    try:
        pass
    except Exception as ex:
        raise Unauthorized("Invalid or missing token")
