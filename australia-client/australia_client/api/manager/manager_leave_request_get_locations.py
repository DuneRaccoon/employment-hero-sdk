from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.location_model import LocationModel
from ...types import Response


def _get_kwargs(
    business_id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/api/v2/business/{business_id}/manager/leaverequest/locations",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[List["LocationModel"]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = LocationModel.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[List["LocationModel"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    business_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[List["LocationModel"]]:
    """List Leave Locations

     Lists all locations of employees this manager has leave permissions on.

    Args:
        business_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['LocationModel']]
    """

    kwargs = _get_kwargs(
        business_id=business_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    business_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[List["LocationModel"]]:
    """List Leave Locations

     Lists all locations of employees this manager has leave permissions on.

    Args:
        business_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['LocationModel']
    """

    return sync_detailed(
        business_id=business_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    business_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[List["LocationModel"]]:
    """List Leave Locations

     Lists all locations of employees this manager has leave permissions on.

    Args:
        business_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['LocationModel']]
    """

    kwargs = _get_kwargs(
        business_id=business_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    business_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[List["LocationModel"]]:
    """List Leave Locations

     Lists all locations of employees this manager has leave permissions on.

    Args:
        business_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['LocationModel']
    """

    return (
        await asyncio_detailed(
            business_id=business_id,
            client=client,
        )
    ).parsed
