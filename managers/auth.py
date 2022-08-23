from datetime import datetime, timedelta
from decouple import config

import jwt
from flask_httpauth import HTTPTokenAuth
from jwt import ExpiredSignatureError, InvalidTokenError
from werkzeug.exceptions import Unauthorized

# Need these imports for verify_token eval
from models import VehicleOwnerModel
from models import MechanicModel


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
        if not token:
            raise Unauthorized("Missing token")
        try:
            payload = jwt.decode(token, key=config("JWT_SECRET"), algorithms=["HS256"])
            return payload["sub"], payload["type"]
        except ExpiredSignatureError:
            raise Unauthorized("Expired token")
        except InvalidTokenError:
            raise Unauthorized("Invalid token")


auth = HTTPTokenAuth(scheme="Bearer")


@auth.verify_token
def verify_token(token):
    try:
        user_id, type_user = AuthManager.decode_token(token)
        return eval(f"{type_user}.query.filter_by(id={user_id}).first()")
    except Exception as ex:
        raise ex
