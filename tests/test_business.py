import pytest
from ..employment_hero_sdk.apis.business import BusinessManager, Business

# Dummy response class to simulate httpx.Response
class DummyResponse:
    def __init__(self, json_data, status_code=200, headers=None, text=""):
        self._json = json_data
        self.status_code = status_code
        self.headers = headers or {}
        self.text = text

    def json(self):
        return self._json

@pytest.mark.asyncio
async def test_business_list(client, monkeypatch):
    async def dummy_arequest(method, url, **kwargs):
        if url == "/v2/business":
            return DummyResponse({"data": [{"id": "biz1"}, {"id": "biz2"}]})
        return DummyResponse({"data": {}})
    monkeypatch.setattr(client, "_arequest", dummy_arequest)
    
    bm = client.business  # BusinessManager instance.
    businesses = await bm.list()
    assert len(businesses) == 2
    assert businesses[0].business_id == "biz1"
    assert businesses[1].business_id == "biz2"

@pytest.mark.asyncio
async def test_business_employee_chaining(client):
    business_id = "biz123"
    business = client.business(business_id)
    assert business.base_path == f"/v2/business/{business_id}"
    employee_api = business.employee
    assert employee_api.parent_path == f"/v2/business/{business_id}"
