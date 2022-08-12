from db import db
from models import RepairModel


class RepairManager:

    @staticmethod
    def create(data, vehicle_id):
        data["vehicle_id"] = vehicle_id
        repair = RepairModel(**data)
        db.session.add(repair)
        db.session.flush()
        return repair
