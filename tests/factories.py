from random import randint

import factory

from faker import Faker
from faker_vehicle import VehicleProvider

from db import db
from models import VehicleOwnerModel, UserRole, MechanicModel, VehicleModel


class BaseFactory(factory.Factory):

    @classmethod
    def create(cls, **kwargs):
        object = super().create(**kwargs)
        db.session.add(object)
        db.session.commit()
        return object


class VehicleOwnerFactory(BaseFactory):
    class Meta:
        model = VehicleOwnerModel

    id = factory.Sequence(lambda n: n)
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    email = factory.Faker("email")
    phone_number = str(randint(100000, 200000))
    password = factory.Faker("password")
    role = UserRole.vehicle_owner


class MechanicFactory(BaseFactory):
    class Meta:
        model = MechanicModel

    id = factory.Sequence(lambda n: n)
    company_name = factory.Faker("company")
    email = factory.Faker("email")
    phone_number = str(randint(100000, 200000))
    password = factory.Faker("password")
    role = UserRole.mechanic


class VehicleFactory(BaseFactory):
    fake = Faker()
    fake.add_provider(VehicleProvider)

    class Meta:
        model = VehicleModel

    id = factory.Sequence(lambda n: n)
    year_of_registration = randint(1800, 2022)
    vehicle_type = factory.Faker(fake.vehicle_category())
    model = factory.Faker(fake.vehicle_make_model())
