from marshmallow import Schema, fields


class RepairRequestSchema(Schema):
    title = fields.String(required=True)
    description = fields.String(required=True)
    photo = fields.String(required=True)
    extension = fields.String(required=True)


class RepairGetByIdSchema(Schema):
    pass
