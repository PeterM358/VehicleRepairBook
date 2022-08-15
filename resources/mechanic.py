from flask_restful import Resource

from managers.mechanic import MechanicManager
from schemas.responses.mechanic import MechanicsGetResponseSchema


class MechanicsGetResource(Resource):

    @staticmethod
    def get():
        mechanics = MechanicManager.get_mechanics()
        return MechanicsGetResponseSchema().dump(mechanics, many=True), 200
