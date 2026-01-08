import enum


class PropertyType(str, enum.Enum):
    HOUSE = "house"
    APARTMENT = "apartment"
    VILLA = "villa"
    STUDIO = "studio"
    LOFT = "loft"
    DUPLEX = "duplex"
    TRIPLEX = "triplex"
    PENTHOUSE = "penthouse"
    LAND = "land"
    COMMERCIAL = "commercial"
    PARKING = "parking"


class EnergyRating(str, enum.Enum):
    A = "A"
    B = "B"
    C = "C"
    D = "D"
    E = "E"
    F = "F"
    G = "G"


class HeatingType(str, enum.Enum):
    INDIVIDUAL = "individual"
    COLLECTIVE = "collective"
    ELECTRIC = "electric"
    GAS = "gas"
    FUEL = "fuel"
    WOOD = "wood"
    SOLAR = "solar"
    NONE = "none"
    HEAT_PUMP = "heat_pump"


class FeatureCategory(str, enum.Enum):
    COMFORT = "comfort"
    SECURITY = "security"
    EXTERIOR = "exterior"
    KITCHEN = "kitchen"
    BATHROOM = "bathroom"


class TransactionType(str, enum.Enum):
    SALE = "sale"
    RENT = "rent"
