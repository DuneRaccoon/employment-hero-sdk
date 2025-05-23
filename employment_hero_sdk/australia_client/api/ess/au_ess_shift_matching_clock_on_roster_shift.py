import datetime
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.au_roster_shift_matching_result_model import AuRosterShiftMatchingResultModel
from ...types import UNSET, Response


def _get_kwargs(
    employee_id: str,
    *,
    local_time: datetime.datetime,
    allow_not_ended: bool,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_local_time = local_time.isoformat()
    params["localTime"] = json_local_time

    params["allowNotEnded"] = allow_not_ended

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/api/v2/ess/{employee_id}/shift/matchingclockon",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[AuRosterShiftMatchingResultModel]:
    if response.status_code == HTTPStatus.OK:
        response_200 = AuRosterShiftMatchingResultModel.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[AuRosterShiftMatchingResultModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    employee_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    local_time: datetime.datetime,
    allow_not_ended: bool,
) -> Response[AuRosterShiftMatchingResultModel]:
    """Find Matching Clock On Roster Shift

     If a roster shift exists that could match for this employee to clock on at this time
    given ESS settings for shift matching, returns that shift.
    Otherwise, the Shift result will be null.
    Note that if the time matches a shift exactly, the Shift result will also be null.
    However, if allowNotEnded is set to true, the ongoing shift will be returned.

    Args:
        employee_id (str):
        local_time (datetime.datetime):
        allow_not_ended (bool):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AuRosterShiftMatchingResultModel]
    """

    kwargs = _get_kwargs(
        employee_id=employee_id,
        local_time=local_time,
        allow_not_ended=allow_not_ended,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    employee_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    local_time: datetime.datetime,
    allow_not_ended: bool,
) -> Optional[AuRosterShiftMatchingResultModel]:
    """Find Matching Clock On Roster Shift

     If a roster shift exists that could match for this employee to clock on at this time
    given ESS settings for shift matching, returns that shift.
    Otherwise, the Shift result will be null.
    Note that if the time matches a shift exactly, the Shift result will also be null.
    However, if allowNotEnded is set to true, the ongoing shift will be returned.

    Args:
        employee_id (str):
        local_time (datetime.datetime):
        allow_not_ended (bool):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AuRosterShiftMatchingResultModel
    """

    return sync_detailed(
        employee_id=employee_id,
        client=client,
        local_time=local_time,
        allow_not_ended=allow_not_ended,
    ).parsed


async def asyncio_detailed(
    employee_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    local_time: datetime.datetime,
    allow_not_ended: bool,
) -> Response[AuRosterShiftMatchingResultModel]:
    """Find Matching Clock On Roster Shift

     If a roster shift exists that could match for this employee to clock on at this time
    given ESS settings for shift matching, returns that shift.
    Otherwise, the Shift result will be null.
    Note that if the time matches a shift exactly, the Shift result will also be null.
    However, if allowNotEnded is set to true, the ongoing shift will be returned.

    Args:
        employee_id (str):
        local_time (datetime.datetime):
        allow_not_ended (bool):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AuRosterShiftMatchingResultModel]
    """

    kwargs = _get_kwargs(
        employee_id=employee_id,
        local_time=local_time,
        allow_not_ended=allow_not_ended,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    employee_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    local_time: datetime.datetime,
    allow_not_ended: bool,
) -> Optional[AuRosterShiftMatchingResultModel]:
    """Find Matching Clock On Roster Shift

     If a roster shift exists that could match for this employee to clock on at this time
    given ESS settings for shift matching, returns that shift.
    Otherwise, the Shift result will be null.
    Note that if the time matches a shift exactly, the Shift result will also be null.
    However, if allowNotEnded is set to true, the ongoing shift will be returned.

    Args:
        employee_id (str):
        local_time (datetime.datetime):
        allow_not_ended (bool):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AuRosterShiftMatchingResultModel
    """

    return (
        await asyncio_detailed(
            employee_id=employee_id,
            client=client,
            local_time=local_time,
            allow_not_ended=allow_not_ended,
        )
    ).parsed
