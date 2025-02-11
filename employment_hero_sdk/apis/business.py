import time
from typing import List, Optional, Union, Dict, Any
from .base import EmploymentHeroBase
from ..client import EmploymentHeroClient, EmploymentHeroAsyncClient
from ..utils import snake_to_pascal_case, pascal_to_snake_case

class Business(EmploymentHeroBase):
    """
    Represents a specific business in the Employment Hero API.
    Once in a business context, you may chain additional endpoints (e.g. employees, locations, etc.)
    under the business' base path.
    """
    def __init__(
        self,
        business_id: Any,
        *args, 
        **kwargs
    ):
        super().__init__(*args, **kwargs)
        self.business_id = business_id

    @property
    def base_path(self) -> str:
        return f"/api/v2/business/{self.business_id}"

    def __getattr__(self, item: str):
        # Dynamically load a chained endpoint under this business.
        from importlib import import_module
        try:
            base_package = self.client.__class__.__module__.split(".")[0]
            module = import_module(f"{base_package}.apis.{item.lower()}")
            api_class = getattr(module, snake_to_pascal_case(item))
            return api_class(client=self.client, parent_path=self.base_path)
        except (ModuleNotFoundError, AttributeError):
            raise AttributeError(f"No such endpoint '{item}' in business context.")

    def fetch(self) -> "Business":
        """
        Optionally, fetch business details using its business_id.
        """
        if not isinstance(self.client, EmploymentHeroClient):
            raise ValueError("This method requires an sync client.")
        
        url = f"/api/v2/business/{self.business_id}"
        response = self.client._request("GET", url)
        response_data = self._parse_response_data(response.json())
        if len(response_data) == 0:
            raise ValueError(f"Business with id '{self.business_id}' not found.") 
        if len(response_data) > 1:
            raise ValueError(f"Multiple businesses with id '{self.business_id}' found.")
        self.data = response_data[0]
        return self
    
    async def fetch_async(self) -> "Business":
        """
        Optionally, fetch business details using its business_id.
        """
        if not isinstance(self.client, EmploymentHeroAsyncClient):
            raise ValueError("This method requires an async client.")
        
        url = f"/api/v2/business/{self.business_id}"
        response = await self.client._request("GET", url)
        response_data = self._parse_response_data(response.json())
        if len(response_data) == 0:
            raise ValueError(f"Business with id '{self.business_id}' not found.") 
        if len(response_data) > 1:
            raise ValueError(f"Multiple businesses with id '{self.business_id}' found.")
        self.data = response_data[0]
        return self

    def __repr__(self):
        return f"<Business id={self.business_id}>"

class BusinessManager:
    """
    Provides access to business endpoints.
    
    - When called with no argument, returns a coroutine that resolves to the list of available businesses.
    - When called with a business id, returns a coroutine that resolves to that specific business.
    
    The list of businesses is cached for a period (default TTL is 300 seconds) to avoid excess API calls.
    """
    def __init__(self, *, client: EmploymentHeroClient, cache_ttl: int = 300):
        self.client = client
        self._cache: Optional[Dict[Any, Business]] = None
        self._cache_timestamp: float = 0
        self.cache_ttl = cache_ttl
    
    @staticmethod
    def _handle_list_response(response: Dict[str, Any]) -> List[Dict[str, Any]]:
        return response if isinstance(response, list) else [response]

    def all(self, **params) -> Dict[Any, Business]:
        """Retrieve the list of available businesses, using cache if available."""
        current_time = time.time()
        if self._cache is not None and (current_time - self._cache_timestamp) < self.cache_ttl:
            return self._cache

        # The endpoint path for listing businesses is provided as "/api/v2/business"
        url = "/api/v2/business"
        response = self.client._request("GET", url, params=params)
        self._cache = {
            business.business_id: business
            for business in [
                Business(client=self.client, business_id=item.get("id"), data=item)
                for item in self._handle_list_response(response.json())
            ]
        }
        self._cache_timestamp = current_time
        return self._cache

    def get(self, business_id: str) -> Business:
        """Return the business with the given ID (from cache or fetched list)."""
        businesses = self.all()
        biz = businesses.get(business_id)
        if biz:
            return biz
        # Optionally, attempt a direct GET on /v2/business/{business_id} here.
        raise ValueError(f"Business with id '{business_id}' not found.")

    def __call__(self, business_id: Optional[str] = None):
        """
        When the BusinessManager is called:
          - With no argument, returns a coroutine that resolves to the list of businesses.
          - With a business id, returns a coroutine that resolves to that specific business.
          
        Usage:
            businesses = client.business()         # list all businesses (cached)
            biz = client.business("biz123")           # get a specific business
        """
        if business_id is None:
            return self.all()
        else:
            return self.get(business_id)


class AsyncBusinessManager:
    """
    Provides access to business endpoints.
    
    - When called with no argument, returns a coroutine that resolves to the list of available businesses.
    - When called with a business id, returns a coroutine that resolves to that specific business.
    
    The list of businesses is cached for a period (default TTL is 300 seconds) to avoid excess API calls.
    """
    def __init__(self, *, client: EmploymentHeroAsyncClient, cache_ttl: int = 300):
        self.client = client
        self._cache: Optional[Dict[Any, Business]] = None
        self._cache_timestamp: float = 0
        self.cache_ttl = cache_ttl

    @staticmethod
    def _handle_list_response(response: Dict[str, Any]) -> List[Dict[str, Any]]:
        return response if isinstance(response, list) else [response]

    async def all(self, **params) -> Dict[Any, Business]:
        """Retrieve the list of available businesses, using cache if available."""
        current_time = time.time()
        if self._cache is not None and (current_time - self._cache_timestamp) < self.cache_ttl:
            return self._cache

        # The endpoint path for listing businesses is provided as "/api/v2/business"
        url = "/api/v2/business"
        response = await self.client._request("GET", url, params=params)
        data = response.json()
        data_list = data if isinstance(data, list) else response.json().get("data", [])
        self._cache = {
            business.business_id: business
            for business in [
                Business(client=self.client, business_id=item.get("id"), data=item)
                for item in self._handle_list_response(response.json())
            ]
        }
        self._cache_timestamp = current_time
        return self._cache

    async def get(self, business_id: str) -> Business:
        """Return the business with the given ID (from cache or fetched list)."""
        businesses = await self.all()
        biz = businesses.get(business_id)
        if biz:
            return biz
        # Optionally, attempt a direct GET on /v2/business/{business_id} here.
        raise ValueError(f"Business with id '{business_id}' not found.")

    def __call__(self, business_id: Optional[str] = None):
        """
        When the BusinessManager is called:
          - With no argument, returns a coroutine that resolves to the list of businesses.
          - With a business id, returns a coroutine that resolves to that specific business.
          
        Usage:
            businesses = await client.business()         # list all businesses (cached)
            biz = await client.business("biz123")           # get a specific business
        """
        if business_id is None:
            return self.all()
        else:
            return self.get(business_id)
