from flask_testing import TestCase

from config import create_app
from db import db
from tests.factories import VehicleFactory


class TestRepair(TestCase):
    endpoints = (
        ()
    )
    url = "/vehicle/create/"

    def create_app(self):
        return create_app("config.TestConfig")

    def setUp(self) -> None:
        db.init_app(self.app)
        db.create_all()

    def tearDown(self) -> None:
        db.session.remove()
        db.drop_all()

    # def test_create_repair_missing_fields_raises(self):
    #     vehicle = VehicleFactory()
    #     a = 5