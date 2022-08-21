from flask import request
from flask_restful import Resource

from managers.mechanic import MechanicManager
from managers.vehicle_owner import VehicleOwnerManager
from schemas.requests.auth import VehicleOwnerSignUpRequestSchema, MechanicSignUpRequestSchema, \
    VehicleOwnerSignInRequestSchema, MechanicSignInRequestSchema
from utils.decorators import validate_schema


class VehicleOwnerSignUpResource(Resource):
    # TODO validate schema to be inserted
    @validate_schema(VehicleOwnerSignUpRequestSchema)
    def post(self):
        data = request.get_json()
        token = VehicleOwnerManager.sign_up(data)
        return {"token": token}, 201


class VehicleOwnerSignInResource(Resource):
    @validate_schema(VehicleOwnerSignInRequestSchema)
    def post(self):
        data = request.get_json()
        token = VehicleOwnerManager.sign_in(data)
        return {"token": token, "role": "vehicle_owner"}, 200


class MechanicSignUpResource(Resource):
    @validate_schema(MechanicSignUpRequestSchema)
    def post(self):
        data = request.get_json()
        token = MechanicManager.sign_up(data)
        return {"token": token}, 201


class MechanicSignInResource(Resource):
    @validate_schema(MechanicSignInRequestSchema)
    def post(self):
        data = request.get_json()
        token = MechanicManager.sign_in(data)
        return {"token": token, "role": "mechanic"}, 200
