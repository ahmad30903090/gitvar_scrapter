from dataclasses import dataclass

@dataclass
class VillaProperty:

    title: str

    built_area: int
    land_area: int | None

    rooms: int
    age: int

    floor_count: int

    parking: bool
    storage: bool
    elevator: bool

    document_type: str

    district: str
    address: str

    price: int

    description: str