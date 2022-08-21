from sqlalchemy import func

from db import db
from models.enums import OfferStatus


class OfferModel(db.Model):
    __tablename__ = "offer"

    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float, nullable=False)
    text = db.Column(db.Text, nullable=True)
    status = db.Column(db.Enum(OfferStatus), default=OfferStatus.sent, nullable=False)
    created_on = db.Column(db.DateTime, server_default=func.now())
    vehicle_owner_id = db.Column(db.Integer, db.ForeignKey("vehicle_owner.id"), nullable=False)
    repair_id = db.Column(db.Integer, db.ForeignKey("repair.id", ondelete="CASCADE"), nullable=True)
    repair = db.relationship("RepairModel", backref="repair")
    mechanic_id = db.Column(db.Integer, db.ForeignKey("mechanic.id"), nullable=False)
    mechanic = db.relationship("MechanicModel", backref="mechanic")

