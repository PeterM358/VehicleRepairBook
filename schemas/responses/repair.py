from marshmallow import fields, Schema

from schemas.responses.vehicle import VehicleResponseSchema


class RepairResponseSchema(Schema):
    id = fields.Int(required=True)
    title = fields.Str(required=True)
    created_on = fields.DateTime(required=True)
    vehicle = fields.Nested(VehicleResponseSchema)