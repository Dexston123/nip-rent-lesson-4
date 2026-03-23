import pytest

from pydantic import ValidationError
from src.models import Apartment
from src.models import Tenant

def test_apartment_fields():
    data = Apartment(
        key="apart-test",
        name="Test Apartment",
        location="Test Location",
        area_m2=50.0,
        rooms={
            "room-1": {"name": "Living Room", "area_m2": 30.0},
            "room-2": {"name": "Bedroom", "area_m2": 20.0}
        }
    )
    assert data.key == "apart-test"
    assert data.name == "Test Apartment"
    assert data.location == "Test Location"
    assert data.area_m2 == 50.0
    assert len(data.rooms) == 2


def test_apartment_from_dict():
    data = {
        "key": "apart-test",
        "name": "Test Apartment",
        "location": "Test Location",
        "area_m2": 50.0,
        "rooms": {
            "room-1": {"name": "Living Room", "area_m2": 30.0},
            "room-2": {"name": "Bedroom", "area_m2": 20.0}
        }
    }
    apartment = Apartment(**data)
    assert apartment.key == data["key"]
    assert apartment.name == data["name"]
    assert apartment.location == data["location"]
    assert apartment.area_m2 == data["area_m2"]
    assert len(apartment.rooms) == len(data["rooms"])

    data['area_m2'] = "25m2" # Invalid field
    with pytest.raises(ValidationError):
        wrong_apartment = Apartment(**data)


def test_tenant_has_all_fields_filled():
    tenant = Tenant(
        name="Jan Kowalski",
        apartment="A101",
        room="Kuchnia",
        rent_pln=1200.00,
        deposit_pln=2400.00,
        date_agreement_from="2023-01-01",
        date_agreement_to="2024-01-01"
    )
    
    assert tenant.name == "Jan Kowalski"
    assert tenant.apartment == "A101"
    assert tenant.room == "Kuchnia"
    assert tenant.rent_pln == 1200.00
    assert tenant.deposit_pln == 2400.00
    assert tenant.date_agreement_from == "2023-01-01"
    assert tenant.date_agreement_to == "2024-01-01"


def test_tenant_from_dict():
    tenant_data = {
        "name": "Anna Nowak",
        "apartment": "B202",
        "room": "Salon",
        "rent_pln": 1500.00,
        "deposit_pln": 3000.00,
        "date_agreement_from": "2023-02-01",
        "date_agreement_to": "2024-02-01"
    }

    tenant = Tenant(**tenant_data)

    assert tenant.name == "Anna Nowak"
    assert tenant.apartment == "B202"
    assert tenant.rent_pln == 1500.00
    assert tenant.date_agreement_from == "2023-02-01"

    invalid_tenant_data = tenant_data.copy()
    del invalid_tenant_data["room"]

    with pytest.raises(Exception):
        Tenant(**invalid_tenant_data)