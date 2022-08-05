from db import db
from models.enums import UserRole


class BaseUserModel(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)


class VehicleOwnerModel(BaseUserModel):
    __tablename__ = "vehicle_owner"

    vehicles = db.relationship("VehicleModel", backref="vehicle", lazy="dynamic")
    role = db.Column(db.Enum(UserRole), default=UserRole.owner, nullable=False)


# TODO should have relation with user if authorised // also should add some certificates
class MechanicModel(BaseUserModel):
    __tablename__ = "mechanic"

    vehicle_owners = db.relationship("VehicleOwnerModel", backref="vehicle_owner", lazy="dynamic")
    role = db.Column(db.Enum(UserRole), default=UserRole.mechanic, nullable=False)


class AdminModel(BaseUserModel):
    __tablename__ = "admin"
    role = db.Column(db.Enum(UserRole), default=UserRole.admin, nullable=False)
    pass
