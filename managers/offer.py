from werkzeug.exceptions import NotFound

from db import db
from models import RepairModel, VehicleModel
from models.enums import OfferStatus, RepairStatus
from models.offer import OfferModel


class OfferManager:

    @staticmethod
    def create(data, repair_id, mechanic):
        repair = RepairModel.query.filter_by(id=repair_id).first()
        vehicle = VehicleModel.query.filter_by(id=repair.vehicle_id).first()
        vehicle_owner_id = vehicle.vehicle_owner_id
        if not repair:
            raise NotFound("This repair is not existing")
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
    def accept_offer(offer_id):
        offer = OfferModel.query.filter_by(id=offer_id).first()
        OfferModel.query.filter_by(id=offer_id).update({"status": OfferStatus.accepted})
        RepairModel.query.filter_by(id=offer.repair_id).update({"status": RepairStatus.ongoing})

