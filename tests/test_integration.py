import json
from src.models import Apartment
from src.manager import Manager
from src.models import Parameters


def test_load_data():
    parameters = Parameters()
    manager = Manager(parameters)
    assert isinstance(manager.apartments, dict)
    assert isinstance(manager.tenants, dict)
    assert isinstance(manager.transfers, list)
    assert isinstance(manager.bills, list)

    for apartment_key, apartment in manager.apartments.items():
        assert isinstance(apartment, Apartment)
        assert apartment.key == apartment_key


def test_all_tenants_loaded_to_manager():
    parameters = Parameters()
    manager = Manager(parameters)

    with open(parameters.tenants_json_path, 'r') as f:
        tenants_data = json.load(f)

    manager_names = [tenant.name for tenant in manager.tenants.values()]

    for tenant_key, tenant_data in tenants_data.items():
        assert tenant_data["name"] in manager_names