from marshmallow import Schema, fields


class RepairRequestSchema(Schema):
    # vehicle_id = fields.Integer(required=True)
    title = fields.String(required=True)
    description = fields.String(required=True)
    photo_url = fields.String(required=True)
