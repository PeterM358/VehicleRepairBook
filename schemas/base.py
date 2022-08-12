from marshmallow import fields, Schema





# TODO add validators


class AuthBase(Schema):
    email = fields.Email(required=True)
    password = fields.Str(required=True)


class VehicleBase(Schema):
    vehicle_type = fields.Str(required=True)
    model = fields.Str(required=True)
    year_of_registration = fields.Int(required=True)

