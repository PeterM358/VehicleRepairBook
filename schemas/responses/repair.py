from marshmallow import fields, Schema
from marshmallow_enum import EnumField

from models import RepairStatus
from schemas.responses.vehicle import VehicleResponseSchema


class RepairResponseSchema(Schema):
    # TODO add date created on date finished
    id = fields.Int(required=True)
    title = fields.Str(required=True)
    # created_on = fields.DateTime(required=True)
    photo_url = fields.String(required=True)
    status = EnumField(RepairStatus, by_value=True)
    vehicle = fields.Nested(VehicleResponseSchema)


class RepairUpdateResponseSchema(Schema):
    pass


class GetAllRepairsResponseSchema(Schema):
    id = fields.Int(required=True)
    title = fields.Str(required=True)
    status = EnumField(RepairStatus, by_value=True)


