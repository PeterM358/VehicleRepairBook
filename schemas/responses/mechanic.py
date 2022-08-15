from marshmallow import Schema, fields


class MechanicsGetResponseSchema(Schema):
    id = fields.Int(required=True)
    company_name = fields.Str(required=True)
