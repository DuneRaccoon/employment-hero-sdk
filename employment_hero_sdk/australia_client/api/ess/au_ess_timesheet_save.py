from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.ess_timesheet_model import EssTimesheetModel
from ...types import Response


def _get_kwargs(
    employee_id: str,
    *,
    body: Union[
        EssTimesheetModel,
        EssTimesheetModel,
    ],
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/api/v2/ess/{employee_id}/timesheet",
    }

    if isinstance(body, EssTimesheetModel):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, EssTimesheetModel):
        _data_body = body.to_dict()

        _kwargs["data"] = _data_body
        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[Any]:
    if response.status_code == HTTPStatus.OK:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[Any]:
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
    body: Union[
        EssTimesheetModel,
        EssTimesheetModel,
    ],
) -> Response[Any]:
    """Submit or Update Timesheet

     If no ID is specified, create a new timesheet for the employee.
    Otherwise, update the timesheet with the specified ID.

    Args:
        employee_id (str):
        body (EssTimesheetModel):
        body (EssTimesheetModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        employee_id=employee_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    employee_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        EssTimesheetModel,
        EssTimesheetModel,
    ],
) -> Response[Any]:
    """Submit or Update Timesheet

     If no ID is specified, create a new timesheet for the employee.
    Otherwise, update the timesheet with the specified ID.

    Args:
        employee_id (str):
        body (EssTimesheetModel):
        body (EssTimesheetModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        employee_id=employee_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
