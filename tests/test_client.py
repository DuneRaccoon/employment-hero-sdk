import pytest
from employment_hero_sdk.client import EmploymentHeroClient

# def test_client_no_api_key():
#     with pytest.raises(ValueError):
#         EmploymentHeroClient(api_key="")

def test_client_headers(client):
    default_headers = client.headers
    custom_headers = {"X-Test": "value"}
    request_kwargs = client._prepare_request(headers=custom_headers)
    assert "Content-Type" in request_kwargs["headers"]
    assert "Accept" in request_kwargs["headers"]
    assert request_kwargs["headers"]["X-Test"] == "value"
