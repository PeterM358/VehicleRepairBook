from marshmallow import fields, validate

from schemas.base import AuthBase


class VehicleOwnerSignUpRequestSchema(AuthBase):
    first_name = fields.Str(required=True, validate=validate.Length(min=2, max=20))
    last_name = fields.Str(required=True, validate=validate.Length(min=2, max=20))


class VehicleOwnerSignInRequestSchema(AuthBase):
    pass


class MechanicSignUpRequestSchema(AuthBase):
    company_name = fields.Str(required=True, min_length=1, max_length=50)


class MechanicSignInRequestSchema(AuthBase):
    pass
