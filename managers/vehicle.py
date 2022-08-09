from db import db
from models import VehicleModel


class VehicleManager:
    @staticmethod
    def create(data, user):
        data["vehicle_owner_id"] = user.id
        vehicle = VehicleModel(**data)
        db.session.add(vehicle)
        return 201