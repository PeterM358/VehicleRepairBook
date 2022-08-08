import enum


class UserRole(enum.Enum):
    mechanic = "mechanic"
    vehicle_owner = "vehicle_owner"
    admin = "admin"


class RepairStatus(enum.Enum):
    open = "open"
    ongoing = "ongoing"
    completed = "completed"


# TODO list all repair types
class RepairType(enum.Enum):
    tires = "tires"
    pass


class VehicleType(enum.Enum):
    car = "car"
    truck = "truck"
    motorcycle = "motorcycle"
