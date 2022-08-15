from marshmallow import Schema, fields


class CreateVehicleOwnerResponseSchema(Schema):
    id = fields.Str(required=True)
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
