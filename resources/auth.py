from flask import request
from flask_restful import Resource

from managers.vehicle_owner import VehicleOwnerManager


class RegisterResource(Resource):
    def post(self):
        data = request.get_json()
        token = VehicleOwnerManager.register(data)
        return {"token": token}, 201
