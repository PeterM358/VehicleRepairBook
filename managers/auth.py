from datetime import datetime, timedelta
from decouple import config

import jwt
from flask_httpauth import HTTPTokenAuth
from jwt import ExpiredSignatureError, InvalidTokenError
from werkzeug.exceptions import BadRequest, Unauthorized

from models import VehicleOwnerModel, MechanicModel


class AuthManager:
    @staticmethod
    def encode_token(user):
        try:
            payload = {"sub": user.id, "exp": datetime.utcnow() + timedelta(days=2), "type": user.__class__.__name__}
            return jwt.encode(payload, key=config("JWT_SECRET"), algorithm="HS256")
        except Exception as ex:
            return ex

    @staticmethod
    def decode_token(token):
        # TODO fix errors raises
        try:
            payload = jwt.decode(token, key=config("JWT_SECRET"), algorithms=["HS256"])
            return payload["sub"], payload["type"]
        except ExpiredSignatureError:
            raise BadRequest("Token expired")
        except InvalidTokenError:
            raise BadRequest("Invalid token")


auth = HTTPTokenAuth(scheme="Bearer")


@auth.verify_token
def verify_token(token):
    try:
        user_id, type_user = AuthManager.decode_token(token)
        return eval(f"{type_user}.query.filter_by(id={user_id}).first()")
    except Exception as ex:
        raise Unauthorized("Invalid or missing token")
