import os.path
import uuid

from constants.common import TEMP_DIR
from db import db
from models import RepairModel
from services.s3 import S3Service
from utils.common import decode_file


class RepairManager:

    @staticmethod
    def create(data, vehicle_id):
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
            repair = RepairModel(**data)
            db.session.add(repair)
            db.session.flush()
            return repair
        except Exception:
            return s3.delete_photo(file_name)
        finally:
            os.remove(path)
