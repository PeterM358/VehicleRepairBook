from resources.auth import MechanicSignInResource, VehicleOwnerSignUpResource, MechanicSignUpResource, VehicleOwnerSignInResource
from resources.mechanic import MechanicsGetResource
from resources.offer import OfferResource, OffersGetResource, OfferAcceptResource, OfferDeleteResource
from resources.repair import RepairResource, RepairsGetResource, RepairGetByIdResource, RepairDeleteResource
from resources.vehicle import VehicleCreateResource


routes = (
    (VehicleOwnerSignUpResource, "/vehicle_owner/sign_up/"),
    (VehicleOwnerSignInResource, "/vehicle_owner/sign_in/"),
    (MechanicSignUpResource, "/mechanic/sign_up/"),
    (MechanicSignInResource, "/mechanic/sign_in/"),
    (MechanicsGetResource, "/mechanics/"),
    (VehicleCreateResource, "/vehicle/create/"),
    (RepairResource, "/vehicle/<int:id>/repair/"),
    (RepairGetByIdResource, "/repair/<int:id>/"),
    (RepairDeleteResource, "/repair/<int:id>/delete/"),
    (RepairsGetResource, "/repairs/"),
    (OfferResource, "/offer/<int:id>/create/"),
    (OffersGetResource, "/offers/"),
    (OfferAcceptResource, "/offer/<int:id>/accept/"),
    (OfferDeleteResource, "/offer/<int:id>/delete/"),
)

