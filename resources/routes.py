from resources.auth import SignUpVehicleOwnerResource, SignUpMechanicResource

routes = (
    (SignUpVehicleOwnerResource, "/sign_up/vehicle_owner/"),
    (SignUpMechanicResource, "/sign_up/mechanic/"),
)
