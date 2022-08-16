from marshmallow import Schema, fields
from marshmallow_enum import EnumField

from models.enums import OfferStatus


class OfferSchemaResponse(Schema):
    id = fields.Int(required=True)
    price = fields.Float(required=True)
    status = EnumField(OfferStatus, by_value=True)
    repair_id = fields.Int(required=True)
    created_on = fields.DateTime(required=True)
