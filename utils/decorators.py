from flask import request
from werkzeug.exceptions import BadRequest, Forbidden, Unauthorized, NotFound

from managers.auth import auth
from models import VehicleModel


def validate_schema(schema_name):
    def decorated_func(func):
        def wrapper(*args, **kwargs):
            data = request.get_json()
            schema = schema_name()
            errors = schema.validate(data)
            if not errors:
                return func(*args, **kwargs)
            raise BadRequest(errors)
        return wrapper
    return decorated_func


def permission_required(role):
    def decorated_func(func):
        def wrapper(*args, **kwargs):
            current_user = auth.current_user()
            if not current_user.role == role:
                raise Forbidden("Permission denied")
            return func(*args, **kwargs)
        return wrapper
    return decorated_func


def validate_user_has_vehicle():
    def decorated_func(func):
        def wrapper(*args, **kwargs):
            # vehicle_owner = auth.current_user()
            # vehicle = VehicleModel.query.filter_by(id=kwargs["id"]).first()
            # if not vehicle:
            #     raise NotFound("Vehicle is missing or deleted.")
            #
            # if not vehicle.vehicle_owner_id == vehicle_owner.id:
            #     raise Unauthorized("This vehicle does not belong to you.")
            pass

            return func(*args, **kwargs)
        return wrapper
    return decorated_func
