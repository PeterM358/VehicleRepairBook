from resources.auth import MechanicSignInResource, VehicleOwnerSignUpResource, MechanicSignUpResource, VehicleOwnerSignInResource
from resources.mechanic import MechanicsGetResource
from resources.offer import OfferResource, OffersGetResource, OfferAcceptResource, OfferDeleteResource
from resources.repair import RepairResource, RepairsGetResource, RepairGetByIdResource
from resources.vehicle import VehicleCreateResource


routes = (
    (VehicleOwnerSignUpResource, "/vehicle_owner/sign_up/"),
    (VehicleOwnerSignInResource, "/vehicle_owner/sign_in/"),
    (MechanicSignUpResource, "/mechanic/sign_up/"),
    (MechanicSignInResource, "/mechanic/sign_in/"),
    (MechanicsGetResource, "/mechanics/"),
    (VehicleCreateResource, "/vehicle/create/"),
    (RepairResource,
     "/vehicle/<int:id>/repairs/",
     "/vehicle/repairs/",
     "/vehicle/repair/<int:id>/update/",
     "/vehicle/repair/<int:id>/delete/"),
    (RepairGetByIdResource, "/repair/<int:id>/"),
    (RepairsGetResource, "/repairs/"),
    (OfferResource, "/offer/repair/<int:id>/create/"),
    (OffersGetResource, "/offers/"),
    (OfferAcceptResource, "/offer/<int:id>/accept/"),
    (OfferDeleteResource, "/offer/<int:id>/delete/"),
)

