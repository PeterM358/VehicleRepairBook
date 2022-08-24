from flask import request
from flask_restful import Resource

from managers.auth import auth
from managers.repair import RepairManager
from models import UserRole
from schemas.requests.repair import RepairRequestSchema
from schemas.responses.repair import RepairResponseSchema, GetAllRepairsResponseSchema
from utils.decorators import permission_required, validate_schema, check_wrong_or_missing_resource


class RepairResource(Resource):
    """
    Vehicle id should be specified in request url for POST
    Repair id should be specified in request url for PUT and DELETE
    eg: /vehicle/13/repair/create/, /vehicle/repair/50/delete/, /vehicle/repair/51/update/
    """

    # id is vehicle_id
    @auth.login_required
    @permission_required(UserRole.vehicle_owner)
    @validate_schema(RepairRequestSchema)
    def post(self, id):
        data = request.get_json()
        vehicle_owner = auth.current_user()
        new_repair = RepairManager.create(data, id, vehicle_owner.id)
        return RepairResponseSchema().dump(new_repair), 201

    @auth.login_required
    def get(self, id=None):
        if id is None:
            vehicle_owner = auth.current_user()
            repair = RepairManager.get_repairs(vehicle_owner)
            return RepairResponseSchema().dump(repair, many=True), 200

    @auth.login_required
    @permission_required(UserRole.vehicle_owner)
    @check_wrong_or_missing_resource()
    def delete(self, id):
        RepairManager.delete(id)
        return "", 204

    @auth.login_required
    @check_wrong_or_missing_resource()
    def put(self, id):
        data = request.get_json()
        repair = RepairManager.update(data, id,)
        return RepairResponseSchema().dump(repair), 201


class RepairsGetResource(Resource):

    @staticmethod
    def get():
        repairs = RepairManager.get_repairs_index_page()
        return GetAllRepairsResponseSchema().dump(repairs, many=True), 200


class RepairGetByIdResource(Resource):
    @auth.login_required
    @check_wrong_or_missing_resource()
    def get(self, id):
        repair = RepairManager.get_repair_by_id(id)
        return RepairResponseSchema().dump(repair), 200
