from flask_testing import TestCase

from config import create_app
from db import db


class TestApp(TestCase):
    def create_app(self):
        return create_app("config.TestConfig")

    def setUp(self) -> None:
        db.init_app(self.app)
        db.create_all()

    def tearDown(self) -> None:
        db.session.remove()
        db.drop_all()

    def test_login_required(self):
        data = (
            ("/offers/", "GET"),
            ("/vehicle/create/", "POST"),
            ("/vehicle/1/repair/", "POST"),
            ("/repair/1/delete/", "POST"),
            ("/offer/1/create/", "POST"),
            ("/offer/1/accept/", "PUT"),
            ("/offer/1/delete/", "POST"),

        )
        resp = None
        for url, method in data:
            if method == "GET":
                resp = self.client.get(url)
            elif method == "POST":
                resp = self.client.post(url)
            elif method == "PUT":
                resp = self.client.put(url)
            elif method == "DELETE":
                resp = self.client.delete(url)

            self.assert_401(resp)
            self.assertEqual(resp.json, {"message": "Invalid or missing token"})
            # assert resp.status_code == 401
            # assert resp.json == {"message": "Invalid or missing token"}
