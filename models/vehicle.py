from sqlalchemy import func

from db import db


class VehicleModel(db.Model):
    __tablename__ = "vehicle"

    # TODO not finished the model. Should add repairs relaiton here
    id = db.Column(db.Integer, primary_key=True)
    # TODO should validate input data. should be choice field in front end (car, truck, motorcycle)
    vehicle_type = db.Column(db.String, nullable=False)
    model = db.Column(db.String, nullable=False)
    year_of_registration = db.Column(db.Integer, nullable=False)
    created_on = db.Column(db.DateTime, server_default=func.now())
    vehicle_owner_id = db.Column(db.Integer, db.ForeignKey("vehicle_owner.id"), nullable=False)
    # vehicle_owner = db.relationship("VehicleOwnerModel", back_populates="vehicle_owner")
