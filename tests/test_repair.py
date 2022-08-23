from flask_testing import TestCase

from config import create_app
from db import db
from models import RepairModel
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

    def test_create_repair_missing_fields_raises(self):
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

        repairs = RepairModel.query.all()
        assert len(repairs) == 0

    def test_create_repair(self):
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
