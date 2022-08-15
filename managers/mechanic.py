from werkzeug.exceptions import BadRequest
from werkzeug.security import generate_password_hash, check_password_hash

from db import db
from managers.auth import AuthManager
from managers.repair import RepairManager
from models import MechanicModel


class MechanicManager:

    @staticmethod
    def get_mechanics():
        return MechanicModel.query.all()

    @staticmethod
    def sign_up(user_data):
        user_data["password"] = generate_password_hash(user_data["password"])
        user = MechanicModel(**user_data)
        db.session.add(user)
        return AuthManager.encode_token(user)

    @staticmethod
    def sign_in(login_data):
        mechanic = MechanicModel.query.filter_by(email=login_data["email"]).first()
        if not mechanic:
            raise BadRequest("No such email.Please sign up")

        if check_password_hash(mechanic.password, login_data["password"]):
            return AuthManager.encode_token(mechanic)
        raise BadRequest("Wrong credentials!")
