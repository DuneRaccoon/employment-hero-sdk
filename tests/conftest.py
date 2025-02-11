import pytest
from ..employment_hero_sdk.client import EmploymentHeroClient

@pytest.fixture
def api_key():
    return "test_api_key"

@pytest.fixture
def business_id():
    return "test_business_id"

@pytest.fixture
def client(api_key, business_id):
    return EmploymentHeroClient(api_key=api_key, business_id=business_id)
