from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.earnings_line_split_edit_model import EarningsLineSplitEditModel
from ...types import Response


def _get_kwargs(
    business_id: str,
    employee_id: str,
    location_id: int,
    *,
    body: Union[
        EarningsLineSplitEditModel,
        EarningsLineSplitEditModel,
    ],
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": f"/api/v2/business/{business_id}/employee/{employee_id}/earningslinesplit/{location_id}",
    }

    if isinstance(body, EarningsLineSplitEditModel):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, EarningsLineSplitEditModel):
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
    business_id: str,
    employee_id: str,
    location_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        EarningsLineSplitEditModel,
        EarningsLineSplitEditModel,
    ],
) -> Response[Any]:
    """Update Earnings line split

     Updates the employee's earnings line split for the specified location ID.

    Args:
        business_id (str):
        employee_id (str):
        location_id (int):
        body (EarningsLineSplitEditModel):
        body (EarningsLineSplitEditModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        business_id=business_id,
        employee_id=employee_id,
        location_id=location_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    business_id: str,
    employee_id: str,
    location_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        EarningsLineSplitEditModel,
        EarningsLineSplitEditModel,
    ],
) -> Response[Any]:
    """Update Earnings line split

     Updates the employee's earnings line split for the specified location ID.

    Args:
        business_id (str):
        employee_id (str):
        location_id (int):
        body (EarningsLineSplitEditModel):
        body (EarningsLineSplitEditModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        business_id=business_id,
        employee_id=employee_id,
        location_id=location_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
