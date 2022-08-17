from flask import request
from flask_restful import Resource

from managers.auth import auth
from managers.offer import OfferManager
from models import UserRole
from schemas.responses.offer import OfferSchemaResponse
from utils.decorators import permission_required


class OfferResource(Resource):
    # id is repair_id
    @auth.login_required
    @permission_required(UserRole.mechanic)
    def post(self, id):
        data = request.get_json()
        current_user = auth.current_user()
        offer = OfferManager.create(data, id, current_user)
        return OfferSchemaResponse().dump(offer), 201


class OffersGetResource(Resource):

    @auth.login_required
    def get(self):
        offers = OfferManager.get_offers()
        return OfferSchemaResponse().dump(offers, many=True), 201


class OfferAcceptResource(Resource):

    # TODO Check vehicle belongs to owner
    @auth.login_required
    @permission_required(UserRole.vehicle_owner)
    def put(self, id):
        current_user = auth.current_user()
        OfferManager.accept(id, current_user)
        return 204


class OfferDeleteResource(Resource):

    @auth.login_required
    @permission_required(UserRole.mechanic)
    def post(self, id):
        OfferManager.delete(id)
        return 204
