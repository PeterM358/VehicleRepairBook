from flask import request
from flask_restful import Resource

from managers.auth import auth
from managers.repair import RepairManager
from models import UserRole
from schemas.requests.repair import RepairRequestSchema
from schemas.responses.repair import RepairResponseSchema, GetAllRepairsResponseSchema, RepairDeleteResponseSchema
from utils.decorators import permission_required, validate_schema


class RepairResource(Resource):
    @auth.login_required
    @permission_required(UserRole.vehicle_owner)
    @validate_schema(RepairRequestSchema)
    def post(self, id):
        data = request.get_json()
        new_repair = RepairManager.create(data, id)
        return RepairResponseSchema().dump(new_repair), 201

    @auth.login_required
    def get(self, id):
        repair = RepairManager.get(id)
        return RepairResponseSchema().dump(repair, many=True), 200


class RepairDeleteResource(Resource):
    # TODO validate existing id
    @auth.login_required
    def post(self, id):
        repair = RepairManager.delete_repair(id)
        return RepairDeleteResponseSchema().dump(repair), 200


class RepairsGetResource(Resource):

    @staticmethod
    def get():
        repairs = RepairManager.get_repairs()
        return GetAllRepairsResponseSchema().dump(repairs, many=True), 200


class RepairGetByIdResource(Resource):

    def get(self, id):
        repair = RepairManager.get_repair_by_id(id)
        return RepairResponseSchema().dump(repair, many=True), 200

