import phonenumbers
from marshmallow import fields, validate, validates, ValidationError

from schemas.base import AuthBase


class VehicleOwnerSignUpRequestSchema(AuthBase):
    first_name = fields.Str(required=True, validate=validate.Length(min=2, max=20))
    last_name = fields.Str(required=True, validate=validate.Length(min=2, max=20))
    phone_number = fields.Str(required=True)

    @validates("phone_number")
    def validate_phone_number(self, phone_number):
        string_number = phone_number
        phone_number = phonenumbers.parse(string_number)
        if not phonenumbers.is_possible_number(phone_number):
            raise ValidationError("Please provide a valid phone number")


class VehicleOwnerSignInRequestSchema(AuthBase):
    pass


class MechanicSignUpRequestSchema(AuthBase):
    company_name = fields.Str(required=True, min_length=1, max_length=50)
    phone_number = fields.Str(required=True)

    @validates("phone_number")
    def validate_phone_number(self, phone_number):
        string_number = phone_number
        phone_number = phonenumbers.parse(string_number)
        if not phonenumbers.is_possible_number(phone_number):
            raise ValidationError("Please provide a valid phone number")


class MechanicSignInRequestSchema(AuthBase):
    pass
