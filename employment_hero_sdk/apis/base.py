# pyright: reportAttributeAccessIssue=false
from typing import Any, Dict, List, Optional, Type, TypeVar, Union, Coroutine

from ..utils import serialize, deserialize
from ..client import EmploymentHeroClient, EmploymentHeroAsyncClient

T = TypeVar("T", bound="EmploymentHeroBase")

class EmploymentHeroBase:
    """
    Base class for endpoints that require a business parent context.
    
    Child API classes (for example, Employee) should set their own `endpoint`
    attribute (or rely on the default, which is the class name in lowercase).
    
    This class implements standard methods for fetching a single resource,
    listing (or paginating) through resources, and creating/updating/deleting.
    
    Also, its __call__ method is defined so that:
      - If an ID is provided, it returns a single instance (by calling fetch);
      - Otherwise, it returns the list of all resources matching supplied filters.
    """
    endpoint: str = ""

    def __init__(
        self,
        *,
        client: Union[EmploymentHeroClient, EmploymentHeroAsyncClient],
        data: Optional[Dict[str, Any]] = None,
        parent_path: Optional[str] = None  # e.g. "/v2/business/{business_id}"
    ) -> None:
        self.client = client
        self.data: Dict[str, Any] = data or {}
        self.parent_path: Optional[str] = parent_path

    def __getattr__(self, item: str) -> Any:
        if item in self.data:
            return self.data[item]
        raise AttributeError(f"{self.__class__.__name__} has no attribute '{item}'")

    def __repr__(self) -> str:
        identifier = self.data.get("id", "unknown")
        return f"<{self.__class__.__name__} id={identifier}>"

    def __call__(self: T, resource_id: Optional[Any] = None, **kwargs: Any) -> Union[Coroutine[Any, Any, Union[T, List[T]]], Union[T, List[T]]]:
        """
        If a resource_id is provided, fetch and return a single instance;
        otherwise, paginate through all data using the supplied kwargs as filters.
        
        If an async client is supplied, this method returns a coroutine, so you must await it.
        """
        if resource_id is not None:
            return (self.fetch(resource_id) if isinstance(self.client, EmploymentHeroClient) else self.fetch_async(resource_id))
        else:
            return (self.paginate(**kwargs) if isinstance(self.client, EmploymentHeroClient) else self.paginate_async(**kwargs))
        
    @classmethod
    def get_endpoint(cls) -> str:
        return cls.endpoint if cls.endpoint else cls.__name__.lower()

    @staticmethod
    def _parse_response_data(
        response: Union[List[Any], Dict[str, Any]]
    ) -> List[Dict[str, Any]]:
        return response if isinstance(response, list) else [response]

    def _build_url(self, resource_id: Optional[Any] = None, suffix: str = "") -> str:
        if not self.parent_path:
            raise ValueError("Parent path is not defined for a chained endpoint.")
        url = f"{self.parent_path}/{self.get_endpoint()}"
        if resource_id is not None:
            url = f"{url}/{resource_id}"
        if suffix:
            url = f"{url}/{suffix}"
        return url

    def fetch(self: T, resource_id: Any) -> T:
        """Fetch a single resource synchronously by ID."""
        if not isinstance(self.client, EmploymentHeroClient):
            raise ValueError("This method requires a sync client.")
        url = self._build_url(resource_id)
        response = self.client._request("GET", url)
        data = self._parse_response_data(response.json())
        # If the returned data is a list, take the first item.
        if isinstance(data, list):
            data = data[0] if data else {}
        return self.__class__(client=self.client, data=data, parent_path=self.parent_path)  # type: ignore

    async def fetch_async(self: T, resource_id: Any) -> T:
        """Fetch a single resource asynchronously by ID."""
        if not isinstance(self.client, EmploymentHeroAsyncClient):
            raise ValueError("This method requires an async client.")
        url = self._build_url(resource_id)
        response = await self.client._request("GET", url)
        data = self._parse_response_data(response.json())
        if isinstance(data, list):
            data = data[0] if data else {}
        return self.__class__(client=self.client, data=data, parent_path=self.parent_path)  # type: ignore

    def list(self: T, **params: Any) -> List[T]:
        """List (or paginate synchronously) through resources using provided filters."""
        if not isinstance(self.client, EmploymentHeroClient):
            raise ValueError("This method requires a sync client.")
        url = self._build_url()
        response = self.client._request("GET", url, params=params)
        data_list = self._parse_response_data(response.json())
        return [self.__class__(client=self.client, data=item, parent_path=self.parent_path) for item in data_list]  # type: ignore

    async def list_async(self: T, **params: Any) -> List[T]:
        """List (or paginate asynchronously) through resources using provided filters."""
        if not isinstance(self.client, EmploymentHeroAsyncClient):
            raise ValueError("This method requires an async client.")
        url = self._build_url()
        response = await self.client._request("GET", url, params=params)
        data_list = self._parse_response_data(response.json())
        return [self.__class__(client=self.client, data=item, parent_path=self.parent_path) for item in data_list]  # type: ignore

    def create(self: T, payload: Dict[str, Any]) -> T:
        """Create a new resource synchronously."""
        if not isinstance(self.client, EmploymentHeroClient):
            raise ValueError("This method requires a sync client.")
        url = self._build_url()
        response = self.client._request("POST", url, json=serialize(payload))
        data = self._parse_response_data(response.json())
        data = data[0] if data else {}
        return self.__class__(client=self.client, data=data, parent_path=self.parent_path)  # type: ignore

    async def create_async(self: T, payload: Dict[str, Any]) -> T:
        """Create a new resource asynchronously."""
        if not isinstance(self.client, EmploymentHeroAsyncClient):
            raise ValueError("This method requires an async client.")
        url = self._build_url()
        response = await self.client._request("POST", url, json=serialize(payload))
        data = self._parse_response_data(response.json())
        data = data[0] if data else {}
        return self.__class__(client=self.client, data=data, parent_path=self.parent_path)  # type: ignore

    def update(self: T, resource_id: Any, payload: Dict[str, Any]) -> T:
        """Update an existing resource synchronously."""
        if not isinstance(self.client, EmploymentHeroClient):
            raise ValueError("This method requires a sync client.")
        url = self._build_url(resource_id)
        response = self.client._request("PUT", url, json=serialize(payload))
        data = self._parse_response_data(response.json())
        data = data[0] if data else {}
        return self.__class__(client=self.client, data=data, parent_path=self.parent_path)  # type: ignore

    async def update_async(self: T, resource_id: Any, payload: Dict[str, Any]) -> T:
        """Update an existing resource asynchronously."""
        if not isinstance(self.client, EmploymentHeroAsyncClient):
            raise ValueError("This method requires an async client.")
        url = self._build_url(resource_id)
        response = await self.client._request("PUT", url, json=serialize(payload))
        data = self._parse_response_data(response.json())
        data = data[0] if data else {}
        return self.__class__(client=self.client, data=data, parent_path=self.parent_path)  # type: ignore

    def delete(self, resource_id: Any) -> None:
        """Delete a resource synchronously."""
        if not isinstance(self.client, EmploymentHeroClient):
            raise ValueError("This method requires a sync client.")
        url = self._build_url(resource_id)
        self.client._request("DELETE", url)

    async def delete_async(self, resource_id: Any) -> None:
        """Delete a resource asynchronously."""
        if not isinstance(self.client, EmploymentHeroAsyncClient):
            raise ValueError("This method requires an async client.")
        url = self._build_url(resource_id)
        await self.client._request("DELETE", url)

    def paginate(self: T, **params: Any) -> List[T]:
        """Synchronously paginate through all pages of data."""
        if not isinstance(self.client, EmploymentHeroClient):
            raise ValueError("This method requires a sync client.")
        top = params.get("$top", 100)
        skip = params.get("$skip", 0)
        all_items: List[Dict[str, Any]] = []
        while True:
            params["$top"] = top
            params["$skip"] = skip
            url = self._build_url()
            response = self.client._request("GET", url, params=params)
            page_data = self._parse_response_data(response.json())
            if not page_data:
                break
            all_items.extend(page_data)
            skip += top
        return [self.__class__(client=self.client, data=item, parent_path=self.parent_path) for item in all_items]  # type: ignore

    async def paginate_async(self: T, **params: Any) -> List[T]:
        """Asynchronously paginate through all pages of data."""
        if not isinstance(self.client, EmploymentHeroAsyncClient):
            raise ValueError("This method requires an async client.")
        top = params.get("$top", 100)
        skip = params.get("$skip", 0)
        all_items: List[Dict[str, Any]] = []
        while True:
            params["$top"] = top
            params["$skip"] = skip
            url = self._build_url()
            response = await self.client._request("GET", url, params=params)
            page_data = self._parse_response_data(response.json())
            if not page_data:
                break
            all_items.extend(page_data)
            skip += top
        return [self.__class__(client=self.client, data=item, parent_path=self.parent_path) for item in all_items]  # type: ignore