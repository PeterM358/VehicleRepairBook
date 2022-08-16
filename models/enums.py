import enum


class UserRole(enum.Enum):
    mechanic = "mechanic"
    vehicle_owner = "vehicle_owner"
    admin = "admin"


class RepairStatus(enum.Enum):
    open = "open"
    ongoing = "ongoing"
    completed = "completed"


class OfferStatus(enum.Enum):
    sent = "sent"
    accepted = "accepted"
    passed = "passed"


# TODO list all repair types
class RepairType(enum.Enum):
    tires = "tires"
    pass
