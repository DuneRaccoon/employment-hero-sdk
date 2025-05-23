from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.public_holiday_model import PublicHolidayModel
from ...types import Response


def _get_kwargs(
    business_id: str,
    id: int,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/api/v2/business/{business_id}/publicholiday/{id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PublicHolidayModel]:
    if response.status_code == HTTPStatus.OK:
        response_200 = PublicHolidayModel.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PublicHolidayModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    business_id: str,
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[PublicHolidayModel]:
    """Get Public Holiday Details

     Gets the details for a public holiday with a specific ID

    Args:
        business_id (str):
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PublicHolidayModel]
    """

    kwargs = _get_kwargs(
        business_id=business_id,
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    business_id: str,
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[PublicHolidayModel]:
    """Get Public Holiday Details

     Gets the details for a public holiday with a specific ID

    Args:
        business_id (str):
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PublicHolidayModel
    """

    return sync_detailed(
        business_id=business_id,
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    business_id: str,
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[PublicHolidayModel]:
    """Get Public Holiday Details

     Gets the details for a public holiday with a specific ID

    Args:
        business_id (str):
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PublicHolidayModel]
    """

    kwargs = _get_kwargs(
        business_id=business_id,
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    business_id: str,
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[PublicHolidayModel]:
    """Get Public Holiday Details

     Gets the details for a public holiday with a specific ID

    Args:
        business_id (str):
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PublicHolidayModel
    """

    return (
        await asyncio_detailed(
            business_id=business_id,
            id=id,
            client=client,
        )
    ).parsed
