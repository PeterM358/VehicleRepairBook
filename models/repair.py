from db import db

from models.enums import RepairStatus


class RepairModel(db.Model):
    __tablename__ = "repair"
    # TODO add date created date finished
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=True)
    photo_url = db.Column(db.String(255), nullable=False)
    status = db.Column(db.Enum(RepairStatus), default=RepairStatus.open, nullable=False)
    vehicle_id = db.Column(db.Integer, db.ForeignKey("vehicle.id"), nullable=False)
    vehicle = db.relationship("VehicleModel", backref="vehicle")

