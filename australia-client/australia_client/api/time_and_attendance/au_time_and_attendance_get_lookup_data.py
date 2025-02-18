from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.au_time_and_attendance_lookup_data_model import AuTimeAndAttendanceLookupDataModel
from ...types import Response


def _get_kwargs(
    business_id: str,
    kiosk_id: int,
    employee_id: int,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/api/v2/business/{business_id}/kiosk/{kiosk_id}/lookupdata/{employee_id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[AuTimeAndAttendanceLookupDataModel]:
    if response.status_code == HTTPStatus.OK:
        response_200 = AuTimeAndAttendanceLookupDataModel.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[AuTimeAndAttendanceLookupDataModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    business_id: str,
    kiosk_id: int,
    employee_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[AuTimeAndAttendanceLookupDataModel]:
    """Get Employee Lookup Data

     Gets relevant lookup data for an employee in relation to a kiosk.

    Args:
        business_id (str):
        kiosk_id (int):
        employee_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AuTimeAndAttendanceLookupDataModel]
    """

    kwargs = _get_kwargs(
        business_id=business_id,
        kiosk_id=kiosk_id,
        employee_id=employee_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    business_id: str,
    kiosk_id: int,
    employee_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[AuTimeAndAttendanceLookupDataModel]:
    """Get Employee Lookup Data

     Gets relevant lookup data for an employee in relation to a kiosk.

    Args:
        business_id (str):
        kiosk_id (int):
        employee_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AuTimeAndAttendanceLookupDataModel
    """

    return sync_detailed(
        business_id=business_id,
        kiosk_id=kiosk_id,
        employee_id=employee_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    business_id: str,
    kiosk_id: int,
    employee_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[AuTimeAndAttendanceLookupDataModel]:
    """Get Employee Lookup Data

     Gets relevant lookup data for an employee in relation to a kiosk.

    Args:
        business_id (str):
        kiosk_id (int):
        employee_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AuTimeAndAttendanceLookupDataModel]
    """

    kwargs = _get_kwargs(
        business_id=business_id,
        kiosk_id=kiosk_id,
        employee_id=employee_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    business_id: str,
    kiosk_id: int,
    employee_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[AuTimeAndAttendanceLookupDataModel]:
    """Get Employee Lookup Data

     Gets relevant lookup data for an employee in relation to a kiosk.

    Args:
        business_id (str):
        kiosk_id (int):
        employee_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AuTimeAndAttendanceLookupDataModel
    """

    return (
        await asyncio_detailed(
            business_id=business_id,
            kiosk_id=kiosk_id,
            employee_id=employee_id,
            client=client,
        )
    ).parsed
