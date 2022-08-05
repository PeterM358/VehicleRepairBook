from werkzeug.security import generate_password_hash

from db import db
from managers.auth import AuthManager
from models import VehicleOwnerModel


class VehicleOwnerManager:
    @staticmethod
    def register(user_data):
        user_data["password"] = generate_password_hash(user_data["password"])
        user = VehicleOwnerModel(**user_data)
        db.session.add(user)
        return AuthManager.encode_token(user)

    @staticmethod
    def login(login_data):
        pass
