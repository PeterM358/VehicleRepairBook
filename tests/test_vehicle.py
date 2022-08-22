from flask_testing import TestCase

from config import create_app
from db import db
from tests.factories import VehicleOwnerFactory
from tests.helpers import generate_token


class TestVehicle(TestCase):
    url = "/vehicle/create/"

    def create_app(self):
        return create_app("config.TestConfig")

    def setUp(self) -> None:
        db.init_app(self.app)
        db.create_all()

    def tearDown(self) -> None:
        db.session.remove()
        db.drop_all()

    def test_create_vehicle(self):

        user = VehicleOwnerFactory()
        token = generate_token(user)
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
        data = {
            "year_of_registration": 1988,
            "vehicle_type": "car",
            "model": "Citroen",
        }
        resp = self.client.post(self.url, headers=headers, json=data)
        # self.assert_201(resp)
        assert resp.status_code == 201
