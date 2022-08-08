from werkzeug.security import generate_password_hash

from db import db
from managers.auth import AuthManager
from models import MechanicModel


class MechanicManager:
    @staticmethod
    def sign_up(user_data):
        user_data["password"] = generate_password_hash(user_data["password"])
        user = MechanicModel(**user_data)
        db.session.add(user)
        return AuthManager.encode_token(user)