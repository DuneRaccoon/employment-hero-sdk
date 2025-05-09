from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.roster_shift_edit_model import RosterShiftEditModel
from ...types import UNSET, Response


def _get_kwargs(
    business_id: str,
    roster_shift_id: int,
    *,
    body: Union[
        RosterShiftEditModel,
        RosterShiftEditModel,
    ],
    publish: bool,
    clear_breaks: bool,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    params: Dict[str, Any] = {}

    params["publish"] = publish

    params["clearBreaks"] = clear_breaks

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": f"/api/v2/business/{business_id}/manager/rostershift/{roster_shift_id}",
        "params": params,
    }

    if isinstance(body, RosterShiftEditModel):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, RosterShiftEditModel):
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
    roster_shift_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        RosterShiftEditModel,
        RosterShiftEditModel,
    ],
    publish: bool,
    clear_breaks: bool,
) -> Response[Any]:
    """Update roster shift

     Update an individual roster shift

    Args:
        business_id (str):
        roster_shift_id (int):
        publish (bool):
        clear_breaks (bool):
        body (RosterShiftEditModel):
        body (RosterShiftEditModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        business_id=business_id,
        roster_shift_id=roster_shift_id,
        body=body,
        publish=publish,
        clear_breaks=clear_breaks,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    business_id: str,
    roster_shift_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        RosterShiftEditModel,
        RosterShiftEditModel,
    ],
    publish: bool,
    clear_breaks: bool,
) -> Response[Any]:
    """Update roster shift

     Update an individual roster shift

    Args:
        business_id (str):
        roster_shift_id (int):
        publish (bool):
        clear_breaks (bool):
        body (RosterShiftEditModel):
        body (RosterShiftEditModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        business_id=business_id,
        roster_shift_id=roster_shift_id,
        body=body,
        publish=publish,
        clear_breaks=clear_breaks,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
