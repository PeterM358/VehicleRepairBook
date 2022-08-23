from flask_testing import TestCase

from config import create_app
from db import db
from tests.factories import MechanicFactory
from tests.helpers import generate_token

ENDPOINTS_DATA = (
        ("/offers/", "GET"),
        ("/vehicle/create/", "POST"),
        ("/vehicle/1/repair/create/", "POST"),
        ("/vehicle/repairs/", "GET"),
        ("/vehicle/repair/1/update/", "PUT"),
        ("/vehicle/repair/1/delete/", "DELETE"),
        ("/offer/repair/1/create/", "POST"),
        ("/offer/1/accept/", "PUT"),
        ("/offer/1/delete/", "DELETE"),
)


class TestApp(TestCase):
    def create_app(self):
        return create_app("config.TestConfig")

    def setUp(self) -> None:
        db.init_app(self.app)
        db.create_all()

    def tearDown(self) -> None:
        db.session.remove()
        db.drop_all()

    def iterate_endpoints(
            self,
            endpoints_data,
            status_code_method,
            expected_resp_body,
            headers=None,
            payload=None,
    ):
        if not headers:
            headers = {}
        if not payload:
            payload = {}

        resp = None
        for url, method in endpoints_data:
            if method == "GET":
                resp = self.client.get(url, headers=headers)
            elif method == "POST":
                resp = self.client.post(url, headers=headers)
            elif method == "PUT":
                resp = self.client.put(url, headers=headers)
            elif method == "DELETE":
                resp = self.client.delete(url, headers=headers)
            status_code_method(resp)
            self.assertEqual(resp.json, expected_resp_body)

    def test_login_required_raises_401(self):
        self.iterate_endpoints(
            ENDPOINTS_DATA, self.assert_401, {"message": "Missing token"}
        )

    def test_invalid_token_raises_401(self):
        headers = {"Authorization": "Bearer asdfa132414"}
        self.iterate_endpoints(
            ENDPOINTS_DATA, self.assert_401, {"message": "Invalid token"}, headers
        )

    # TODO check this test with expired token
    def test_expired_token_raises_401(self):
        token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOjQsImV4cCI6MTY2MTI2ODk2MSwidHlwZSI6Ik1lY2hhbmljTW9kZWwifQ.cQn5kHXbL71m-qG6_6dTLS5evZPl9IaZt5YCq6FlgKc"
        headers = {"Authorization": f"Bearer {token}"}
        self.iterate_endpoints(
            ENDPOINTS_DATA, self.assert_401, {"message": "Expired token"}, headers
        )

    def test_missing_permissions_for_mechanics_raises_403(self):
        endpoints_data = (
            ("/vehicle/create/", "POST"),
            ("/vehicle/1/repair/create/", 'POST'),
            ("/vehicle/repair/1/delete/", "DELETE"),
            ("/offer/1/accept/", "PUT")
        )
        mechanic = MechanicFactory()
        token = generate_token(mechanic)
        headers = {"Authorization": f"Bearer {token}"}
        self.iterate_endpoints(
            endpoints_data, self.assert_403, {"message": "Permission denied"}, headers
        )
