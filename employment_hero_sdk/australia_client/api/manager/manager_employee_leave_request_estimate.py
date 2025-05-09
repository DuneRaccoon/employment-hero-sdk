import datetime
from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.manager_leave_estimate import ManagerLeaveEstimate
from ...types import UNSET, Response


def _get_kwargs(
    business_id: str,
    employee_id: int,
    *,
    from_date: datetime.datetime,
    to_date: datetime.datetime,
    leave_category_id: int,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_from_date = from_date.isoformat()
    params["fromDate"] = json_from_date

    json_to_date = to_date.isoformat()
    params["toDate"] = json_to_date

    params["leaveCategoryId"] = leave_category_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/api/v2/business/{business_id}/manager/{employee_id}/leaverequest/estimate",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[ManagerLeaveEstimate]:
    if response.status_code == HTTPStatus.OK:
        response_200 = ManagerLeaveEstimate.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[ManagerLeaveEstimate]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    business_id: str,
    employee_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    from_date: datetime.datetime,
    to_date: datetime.datetime,
    leave_category_id: int,
) -> Response[ManagerLeaveEstimate]:
    """Estimate Leave Hours

     Estimates the number of hours of leave required based on date and leave category.

    Args:
        business_id (str):
        employee_id (int):
        from_date (datetime.datetime):
        to_date (datetime.datetime):
        leave_category_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ManagerLeaveEstimate]
    """

    kwargs = _get_kwargs(
        business_id=business_id,
        employee_id=employee_id,
        from_date=from_date,
        to_date=to_date,
        leave_category_id=leave_category_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    business_id: str,
    employee_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    from_date: datetime.datetime,
    to_date: datetime.datetime,
    leave_category_id: int,
) -> Optional[ManagerLeaveEstimate]:
    """Estimate Leave Hours

     Estimates the number of hours of leave required based on date and leave category.

    Args:
        business_id (str):
        employee_id (int):
        from_date (datetime.datetime):
        to_date (datetime.datetime):
        leave_category_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ManagerLeaveEstimate
    """

    return sync_detailed(
        business_id=business_id,
        employee_id=employee_id,
        client=client,
        from_date=from_date,
        to_date=to_date,
        leave_category_id=leave_category_id,
    ).parsed


async def asyncio_detailed(
    business_id: str,
    employee_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    from_date: datetime.datetime,
    to_date: datetime.datetime,
    leave_category_id: int,
) -> Response[ManagerLeaveEstimate]:
    """Estimate Leave Hours

     Estimates the number of hours of leave required based on date and leave category.

    Args:
        business_id (str):
        employee_id (int):
        from_date (datetime.datetime):
        to_date (datetime.datetime):
        leave_category_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ManagerLeaveEstimate]
    """

    kwargs = _get_kwargs(
        business_id=business_id,
        employee_id=employee_id,
        from_date=from_date,
        to_date=to_date,
        leave_category_id=leave_category_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    business_id: str,
    employee_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    from_date: datetime.datetime,
    to_date: datetime.datetime,
    leave_category_id: int,
) -> Optional[ManagerLeaveEstimate]:
    """Estimate Leave Hours

     Estimates the number of hours of leave required based on date and leave category.

    Args:
        business_id (str):
        employee_id (int):
        from_date (datetime.datetime):
        to_date (datetime.datetime):
        leave_category_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ManagerLeaveEstimate
    """

    return (
        await asyncio_detailed(
            business_id=business_id,
            employee_id=employee_id,
            client=client,
            from_date=from_date,
            to_date=to_date,
            leave_category_id=leave_category_id,
        )
    ).parsed
