from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.au_ess_roster_shift_model import AuEssRosterShiftModel
from ...types import Response


def _get_kwargs(
    employee_id: str,
    shift_id: int,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/api/v2/ess/{employee_id}/shift/{shift_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[AuEssRosterShiftModel]:
    if response.status_code == HTTPStatus.OK:
        response_200 = AuEssRosterShiftModel.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[AuEssRosterShiftModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    employee_id: str,
    shift_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[AuEssRosterShiftModel]:
    """Get Roster Shift by ID

     Gets the roster shift with the specified ID (as long as it is assigned to this employee).

    Args:
        employee_id (str):
        shift_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AuEssRosterShiftModel]
    """

    kwargs = _get_kwargs(
        employee_id=employee_id,
        shift_id=shift_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    employee_id: str,
    shift_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[AuEssRosterShiftModel]:
    """Get Roster Shift by ID

     Gets the roster shift with the specified ID (as long as it is assigned to this employee).

    Args:
        employee_id (str):
        shift_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AuEssRosterShiftModel
    """

    return sync_detailed(
        employee_id=employee_id,
        shift_id=shift_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    employee_id: str,
    shift_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[AuEssRosterShiftModel]:
    """Get Roster Shift by ID

     Gets the roster shift with the specified ID (as long as it is assigned to this employee).

    Args:
        employee_id (str):
        shift_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AuEssRosterShiftModel]
    """

    kwargs = _get_kwargs(
        employee_id=employee_id,
        shift_id=shift_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    employee_id: str,
    shift_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[AuEssRosterShiftModel]:
    """Get Roster Shift by ID

     Gets the roster shift with the specified ID (as long as it is assigned to this employee).

    Args:
        employee_id (str):
        shift_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AuEssRosterShiftModel
    """

    return (
        await asyncio_detailed(
            employee_id=employee_id,
            shift_id=shift_id,
            client=client,
        )
    ).parsed
