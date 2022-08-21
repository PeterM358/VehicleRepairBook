import os.path
import uuid

from werkzeug.exceptions import NotFound, Unauthorized

from constants.common import TEMP_DIR
from db import db
from models import RepairModel
from services.s3 import S3Service
from utils.common import decode_file


class RepairManager:

    # Returns all repairs for vehicle selected by vehicle_owner
    @staticmethod
    def get_repairs(vehicle_owner):
        return RepairModel.query.filter_by(vehicle_owner_id=vehicle_owner.id)

    # Returns all repairs for main pages
    # @staticmethod
    # def get_repairs():
    #     return RepairModel.query.all()

    # TODO May be dont need this/ is front end querying the all repairs object get_repairs?
    @staticmethod
    def get_repair_by_id(repair_id):
        repair = RepairModel.query.filter_by(id=repair_id).first()
        if not repair:
            raise NotFound("This repair is missing")
        return repair

    @staticmethod
    def create(data, vehicle_id, vehicle_owner_id):
        data["vehicle_id"] = vehicle_id
        extension = data.pop("extension")
        photo = data.pop("photo")
        file_name = f"{str(uuid.uuid4())}.{extension}"
        path = os.path.join(TEMP_DIR, file_name)
        decode_file(path, photo)
        s3 = S3Service()
        photo_url = s3.upload_photo(path, file_name)
        try:
            data["photo_url"] = photo_url
            data["vehicle_owner_id"] = vehicle_owner_id
            repair = RepairModel(**data)
            db.session.add(repair)
            db.session.flush()
            return repair
        except Exception:
            return s3.delete_photo(file_name)
        finally:
            os.remove(path)

    @staticmethod
    def delete(repair_id, vehicle_owner):
        repair = RepairModel.query.filter_by(id=repair_id).first()
        if not repair:
            raise NotFound("This repair object is missing.")
        if not repair.vehicle_owner_id == vehicle_owner.id:
            raise Unauthorized("This repair belongs to another user.")
        db.session.delete(repair)

    @staticmethod
    def update(data, repair_id, vehicle_owner):
        repair = RepairModel.query.filter_by(id=repair_id).first()
        if not repair:
            raise NotFound("This repair object is missing.")
        if not repair.vehicle_owner_id == vehicle_owner.id:
            raise Unauthorized("This repair belongs to another user.")
        repair.title = data["title"]
        db.session.flush()
        return repair
