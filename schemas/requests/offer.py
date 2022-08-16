from marshmallow import Schema, fields


class OfferRequestSchema(Schema):
    price = fields.Float(required=True)
    text = fields.String(required=False)
