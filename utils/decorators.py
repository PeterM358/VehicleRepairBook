from flask import request
from werkzeug.exceptions import BadRequest, Forbidden, NotFound, Unauthorized

from managers.auth import auth
from models import RepairModel


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


def check_wrong_or_missing_resource():
    def decorated_func(func):
        def wrapper(*args, **kwargs):
            repair_id = kwargs["id"]
            repair = RepairModel.query.get(repair_id)
            vehicle_owner = auth.current_user()
            if not repair:
                raise NotFound(f"Repair with id:{repair_id} is missing or deleted.")
            if not repair.vehicle_owner_id == vehicle_owner.id:
                raise Unauthorized(f"Repair with id:{repair_id} belongs to another user.")
            return func(*args, **kwargs)

        return wrapper

    return decorated_func
