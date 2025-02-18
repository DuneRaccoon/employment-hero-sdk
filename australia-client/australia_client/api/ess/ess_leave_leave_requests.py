import datetime
from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.ess_leave_request_model import EssLeaveRequestModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    employee_id: str,
    *,
    filter_show_other_employees: Union[Unset, bool] = UNSET,
    filter_approved_only: Union[Unset, bool] = UNSET,
    filter_from_date: Union[Unset, datetime.datetime] = UNSET,
    filter_to_date: Union[Unset, datetime.datetime] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["filter.showOtherEmployees"] = filter_show_other_employees

    params["filter.approvedOnly"] = filter_approved_only

    json_filter_from_date: Union[Unset, str] = UNSET
    if not isinstance(filter_from_date, Unset):
        json_filter_from_date = filter_from_date.isoformat()
    params["filter.fromDate"] = json_filter_from_date

    json_filter_to_date: Union[Unset, str] = UNSET
    if not isinstance(filter_to_date, Unset):
        json_filter_to_date = filter_to_date.isoformat()
    params["filter.toDate"] = json_filter_to_date

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/api/v2/ess/{employee_id}/leave",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[List["EssLeaveRequestModel"]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = EssLeaveRequestModel.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[List["EssLeaveRequestModel"]]:
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
    filter_show_other_employees: Union[Unset, bool] = UNSET,
    filter_approved_only: Union[Unset, bool] = UNSET,
    filter_from_date: Union[Unset, datetime.datetime] = UNSET,
    filter_to_date: Union[Unset, datetime.datetime] = UNSET,
) -> Response[List["EssLeaveRequestModel"]]:
    """List Leave Requests

     Lists all leave requests for this employee, with optional filters

    Args:
        employee_id (str):
        filter_show_other_employees (Union[Unset, bool]):
        filter_approved_only (Union[Unset, bool]):
        filter_from_date (Union[Unset, datetime.datetime]):
        filter_to_date (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['EssLeaveRequestModel']]
    """

    kwargs = _get_kwargs(
        employee_id=employee_id,
        filter_show_other_employees=filter_show_other_employees,
        filter_approved_only=filter_approved_only,
        filter_from_date=filter_from_date,
        filter_to_date=filter_to_date,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    employee_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    filter_show_other_employees: Union[Unset, bool] = UNSET,
    filter_approved_only: Union[Unset, bool] = UNSET,
    filter_from_date: Union[Unset, datetime.datetime] = UNSET,
    filter_to_date: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[List["EssLeaveRequestModel"]]:
    """List Leave Requests

     Lists all leave requests for this employee, with optional filters

    Args:
        employee_id (str):
        filter_show_other_employees (Union[Unset, bool]):
        filter_approved_only (Union[Unset, bool]):
        filter_from_date (Union[Unset, datetime.datetime]):
        filter_to_date (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['EssLeaveRequestModel']
    """

    return sync_detailed(
        employee_id=employee_id,
        client=client,
        filter_show_other_employees=filter_show_other_employees,
        filter_approved_only=filter_approved_only,
        filter_from_date=filter_from_date,
        filter_to_date=filter_to_date,
    ).parsed


async def asyncio_detailed(
    employee_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    filter_show_other_employees: Union[Unset, bool] = UNSET,
    filter_approved_only: Union[Unset, bool] = UNSET,
    filter_from_date: Union[Unset, datetime.datetime] = UNSET,
    filter_to_date: Union[Unset, datetime.datetime] = UNSET,
) -> Response[List["EssLeaveRequestModel"]]:
    """List Leave Requests

     Lists all leave requests for this employee, with optional filters

    Args:
        employee_id (str):
        filter_show_other_employees (Union[Unset, bool]):
        filter_approved_only (Union[Unset, bool]):
        filter_from_date (Union[Unset, datetime.datetime]):
        filter_to_date (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['EssLeaveRequestModel']]
    """

    kwargs = _get_kwargs(
        employee_id=employee_id,
        filter_show_other_employees=filter_show_other_employees,
        filter_approved_only=filter_approved_only,
        filter_from_date=filter_from_date,
        filter_to_date=filter_to_date,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    employee_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    filter_show_other_employees: Union[Unset, bool] = UNSET,
    filter_approved_only: Union[Unset, bool] = UNSET,
    filter_from_date: Union[Unset, datetime.datetime] = UNSET,
    filter_to_date: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[List["EssLeaveRequestModel"]]:
    """List Leave Requests

     Lists all leave requests for this employee, with optional filters

    Args:
        employee_id (str):
        filter_show_other_employees (Union[Unset, bool]):
        filter_approved_only (Union[Unset, bool]):
        filter_from_date (Union[Unset, datetime.datetime]):
        filter_to_date (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['EssLeaveRequestModel']
    """

    return (
        await asyncio_detailed(
            employee_id=employee_id,
            client=client,
            filter_show_other_employees=filter_show_other_employees,
            filter_approved_only=filter_approved_only,
            filter_from_date=filter_from_date,
            filter_to_date=filter_to_date,
        )
    ).parsed
