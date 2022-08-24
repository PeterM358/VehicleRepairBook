from unittest.mock import patch

from flask_testing import TestCase

from config import create_app
from db import db
from models import RepairModel, RepairStatus, VehicleOwnerModel
from services.s3 import S3Service
from tests.factories import VehicleFactory, VehicleOwnerFactory
from tests.helpers import generate_token, encoded_photo, encoded_photo_extension


class TestRepair(TestCase):
    endpoints = (
        ("/vehicle/<int:id>/repair/create/", "POST"),
        ("/vehicle/repairs/", "GET"),
        ("/vehicle/repair/<int:id>/update/", "PUT"),
        ("/vehicle/repair/<int:id>/delete/", "DELETE")
    )

    def create_app(self):
        return create_app("config.TestConfig")

    def setUp(self) -> None:
        db.init_app(self.app)
        db.create_all()

    def tearDown(self) -> None:
        db.session.remove()
        db.drop_all()

    def test_create_repair_missing_schema_fields_raises(self):
        repairs = RepairModel.query.all()
        assert len(repairs) == 0

        owner = VehicleOwnerFactory()
        token = generate_token(owner)
        vehicle = VehicleFactory()
        url = f"/vehicle/{vehicle.id}/repair/create/"
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

        data = {}
        resp = self.client.post(url, headers=headers, json=data)
        self.assert400(resp)

        assert resp.json["message"] == {
            "description": [
                "Missing data for required field."
            ],
            "photo": [
                "Missing data for required field."
            ],
            "title": [
                "Missing data for required field."
            ],
            "extension": [
                "Missing data for required field."
            ]
        }

        repairs = RepairModel.query.all()
        assert len(repairs) == 0

    @patch.object(S3Service, "upload_photo", return_value="test.s3.url")
    def test_create_repair(self, mocked_s3):
        owner = VehicleOwnerFactory()
        token = generate_token(owner)
        vehicle = VehicleFactory()
        url = f"/vehicle/{vehicle.id}/repair/create/"
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
        data = {
            "title": "Oil change",
            "description": "Overdue oil change",
            "photo": encoded_photo,
            "extension": encoded_photo_extension
        }
        resp = self.client.post(url, headers=headers, json=data)
        assert resp.status_code == 201

        resp = resp.json
        remove_created_on_path = ["vehicle", "created_on"]

        current_level = resp
        for key in remove_created_on_path[:-1]:
            current_level = current_level[key]
        current_level.pop(remove_created_on_path[-1])

        expected_response = {
            'description': data["description"],
            "title": data["title"],
            "status": "open",
            "vehicle": {
                "model": vehicle.model,
                "vehicle_type": vehicle.vehicle_type,
                "year_of_registration": vehicle.year_of_registration,
                "id": vehicle.id
            },
            "id": resp["id"],
            "photo_url": mocked_s3.return_value
        }
        assert resp == expected_response
