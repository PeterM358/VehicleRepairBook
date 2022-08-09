from db import db
from models.enums import UserRole


class BaseUserModel(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)


# TODO should on delete cascade
vehicle_owner_mechanic = db.Table(
    "owner_mechanic",
    db.Column("vehicle_owner_id", db.Integer, db.ForeignKey("vehicle_owner.id")),
    db.Column("mechanic", db.Integer, db.ForeignKey("mechanic.id"))
)


class VehicleOwnerModel(BaseUserModel):
    __tablename__ = "vehicle_owner"

    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    vehicles = db.relationship("VehicleModel", back_populates="vehicle_owner", lazy="dynamic")
    role = db.Column(db.Enum(UserRole), default=UserRole.vehicle_owner, nullable=False)


# TODO should have relation with user if authorised // also should add some certificates
class MechanicModel(BaseUserModel):
    __tablename__ = "mechanic"

    company_name = db.Column(db.String(60), nullable=False)
    role = db.Column(db.Enum(UserRole), default=UserRole.mechanic, nullable=False)


class AdminModel(BaseUserModel):
    __tablename__ = "admin"
    role = db.Column(db.Enum(UserRole), default=UserRole.admin, nullable=False)
