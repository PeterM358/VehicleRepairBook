from flask import request
from flask_restful import Resource

from managers.auth import auth
from managers.vehicle import VehicleManager
from models import UserRole
from utils.decorators import permission_required


class VehicleCreateResource(Resource):
    # TODO validate schema to be inserted
    @auth.login_required
    @permission_required(UserRole.vehicle_owner)
    def post(self):
        data = request.get_json()
        current_user = auth.current_user()
        new_vehicle = VehicleManager.create(data, current_user)
        return 281