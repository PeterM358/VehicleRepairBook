from werkzeug.exceptions import BadRequest
from werkzeug.security import generate_password_hash, check_password_hash

from db import db
from managers.auth import AuthManager
from models import VehicleOwnerModel


class VehicleOwnerManager:
    @staticmethod
    def sign_up(user_data):
        user_data["password"] = generate_password_hash(user_data["password"])
        user = VehicleOwnerModel(**user_data)
        db.session.add(user)
        return AuthManager.encode_token(user)

    @staticmethod
    def sign_in(login_data):
        vehicle_owner = VehicleOwnerModel.query.filter_by(email=login_data["email"]).first()
        if not vehicle_owner:
            raise BadRequest("No such email.Please sign up")

        if check_password_hash(vehicle_owner.password, login_data["password"]):
            return AuthManager.encode_token(vehicle_owner)
        raise BadRequest("Wrong credentials!")

    def accept_offer(self):
        pass
