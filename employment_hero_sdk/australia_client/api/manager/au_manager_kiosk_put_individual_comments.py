from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.au_individual_timesheet_line_model import AuIndividualTimesheetLineModel
from ...models.timesheet_line_comments_model import TimesheetLineCommentsModel
from ...types import Response


def _get_kwargs(
    business_id: str,
    timesheet_line_id: str,
    *,
    body: Union[
        TimesheetLineCommentsModel,
        TimesheetLineCommentsModel,
    ],
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": f"/api/v2/business/{business_id}/manager/kiosk/timesheetcomments/{timesheet_line_id}",
    }

    if isinstance(body, TimesheetLineCommentsModel):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, TimesheetLineCommentsModel):
        _data_body = body.to_dict()

        _kwargs["data"] = _data_body
        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[AuIndividualTimesheetLineModel]:
    if response.status_code == HTTPStatus.OK:
        response_200 = AuIndividualTimesheetLineModel.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[AuIndividualTimesheetLineModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    business_id: str,
    timesheet_line_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        TimesheetLineCommentsModel,
        TimesheetLineCommentsModel,
    ],
) -> Response[AuIndividualTimesheetLineModel]:
    """Update comments in a timesheet

     Update an individual timesheet line with comments

    Args:
        business_id (str):
        timesheet_line_id (str):
        body (TimesheetLineCommentsModel):
        body (TimesheetLineCommentsModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AuIndividualTimesheetLineModel]
    """

    kwargs = _get_kwargs(
        business_id=business_id,
        timesheet_line_id=timesheet_line_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    business_id: str,
    timesheet_line_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        TimesheetLineCommentsModel,
        TimesheetLineCommentsModel,
    ],
) -> Optional[AuIndividualTimesheetLineModel]:
    """Update comments in a timesheet

     Update an individual timesheet line with comments

    Args:
        business_id (str):
        timesheet_line_id (str):
        body (TimesheetLineCommentsModel):
        body (TimesheetLineCommentsModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AuIndividualTimesheetLineModel
    """

    return sync_detailed(
        business_id=business_id,
        timesheet_line_id=timesheet_line_id,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    business_id: str,
    timesheet_line_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        TimesheetLineCommentsModel,
        TimesheetLineCommentsModel,
    ],
) -> Response[AuIndividualTimesheetLineModel]:
    """Update comments in a timesheet

     Update an individual timesheet line with comments

    Args:
        business_id (str):
        timesheet_line_id (str):
        body (TimesheetLineCommentsModel):
        body (TimesheetLineCommentsModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AuIndividualTimesheetLineModel]
    """

    kwargs = _get_kwargs(
        business_id=business_id,
        timesheet_line_id=timesheet_line_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    business_id: str,
    timesheet_line_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        TimesheetLineCommentsModel,
        TimesheetLineCommentsModel,
    ],
) -> Optional[AuIndividualTimesheetLineModel]:
    """Update comments in a timesheet

     Update an individual timesheet line with comments

    Args:
        business_id (str):
        timesheet_line_id (str):
        body (TimesheetLineCommentsModel):
        body (TimesheetLineCommentsModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AuIndividualTimesheetLineModel
    """

    return (
        await asyncio_detailed(
            business_id=business_id,
            timesheet_line_id=timesheet_line_id,
            client=client,
            body=body,
        )
    ).parsed
