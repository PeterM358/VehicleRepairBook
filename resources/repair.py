from flask import request
from flask_restful import Resource

from managers.auth import auth
from managers.repair import RepairManager
from models import UserRole
from schemas.requests.repair import RepairRequestSchema
from schemas.responses.repair import RepairResponseSchema
from utils.decorators import permission_required, validate_schema


class RepairCreateResource(Resource):
    @auth.login_required
    @permission_required(UserRole.vehicle_owner)
    @validate_schema(RepairRequestSchema)
    def post(self, id):
        data = request.get_json()
        new_repair = RepairManager.create(data, id)
        return RepairResponseSchema().dump(new_repair), 201
