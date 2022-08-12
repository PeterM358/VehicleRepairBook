from resources.auth import MechanicSignInResource, VehicleOwnerSignUpResource, MechanicSignUpResource, VehicleOwnerSignInResource
from resources.repair import RepairCreateResource
from resources.vehicle import VehicleCreateResource

routes = (
    (VehicleOwnerSignUpResource, "/vehicle_owner/sign_up/"),
    (VehicleOwnerSignInResource, "/vehicle_owner/sign_in/"),
    (MechanicSignUpResource, "/mechanic/sign_up/"),
    (MechanicSignInResource, "/mechanic/sign_in/"),
    (VehicleCreateResource, "/vehicle/create/"),
    (RepairCreateResource, "/vehicle/<int:id>/repair/")
)
