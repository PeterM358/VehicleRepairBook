from marshmallow import fields, Schema


# TODO add validators

class AuthBase(Schema):
    email = fields.Email(required=True)
    password = fields.Str(required=True)
