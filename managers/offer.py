from werkzeug.exceptions import NotFound, Unauthorized, Forbidden

from db import db
from models import RepairModel, VehicleModel, MechanicModel
from models.enums import OfferStatus, RepairStatus
from models.offer import OfferModel


class OfferManager:

    @staticmethod
    def create(data, repair_id, mechanic):
        repair = RepairModel.query.filter_by(id=repair_id).first()
        if not repair:
            raise NotFound("This repair is not existing")
        vehicle = VehicleModel.query.filter_by(id=repair.vehicle_id).first()
        vehicle_owner_id = vehicle.vehicle_owner_id
        data["mechanic_id"] = mechanic.id
        data["repair_id"] = repair_id
        data["vehicle_owner_id"] = vehicle_owner_id
        offer = OfferModel(**data)
        db.session.add(offer)
        db.session.flush()
        return offer

    @staticmethod
    def get_offers():
        offers = OfferModel.query.filter_by(status=OfferStatus.sent)
        return offers

    @staticmethod
    def accept(offer_id, vehicle_owner):
        offer = OfferModel.query.get(offer_id)
        mechanic = MechanicModel.query.get(offer.mechanic_id)
        if not offer.vehicle_owner_id == vehicle_owner.id:
            raise Unauthorized("You are not owner of this vehicle")
        OfferModel.query.filter_by(id=offer_id).update({"status": OfferStatus.accepted})
        RepairModel.query.filter_by(id=offer.repair_id).update(
            {
                "status": RepairStatus.ongoing,
                "mechanic_id": mechanic.id
            }
        )
        vehicle_owner.mechanics.append(mechanic)
        db.session.add(vehicle_owner)

    @staticmethod
    def delete(offer_id):
        offer = OfferModel.query.get(offer_id)
        if not offer:
            raise NotFound("This offer is missing or deleted")
        if not offer.status == OfferStatus.sent:
            raise Forbidden("This offer is already accepted. Please Contact vehicle owner")
        db.session.delete(offer)
