from marshmallow import fields
from schemas.base import VehicleBase
from schemas.responses.user import CreateVehicleOwnerResponseSchema


class VehicleResponseSchema(VehicleBase):
    id = fields.Int(required=True)
    created_on = fields.DateTime(required=True)
    vehicle_owner = fields.Nested(CreateVehicleOwnerResponseSchema)
