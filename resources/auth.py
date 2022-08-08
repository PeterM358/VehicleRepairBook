from flask import request
from flask_restful import Resource

from managers.mechanic import MechanicManager
from managers.vehicle_owner import VehicleOwnerManager


class SignUpVehicleOwnerResource(Resource):
    # TODO validate schema to be inserted
    def post(self):
        data = request.get_json()
        token = VehicleOwnerManager.sign_up(data)
        return {"token": token}, 201


class SignUpMechanicResource(Resource):
    def post(self):
        data = request.get_json()
        token = MechanicManager.sign_up(data)
        return {"token": token}, 201
