from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.add_note_model import AddNoteModel
from ...types import Response


def _get_kwargs(
    employee_id: int,
    shift_id: int,
    *,
    body: Union[
        AddNoteModel,
        AddNoteModel,
    ],
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/api/v2/ess/{employee_id}/timeandattendance/shift/{shift_id}/notes",
    }

    if isinstance(body, AddNoteModel):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, AddNoteModel):
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
    employee_id: int,
    shift_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        AddNoteModel,
        AddNoteModel,
    ],
) -> Response[Any]:
    """Add Note to Shift

     Adds a note to an existing shift.

    Args:
        employee_id (int):
        shift_id (int):
        body (AddNoteModel):
        body (AddNoteModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        employee_id=employee_id,
        shift_id=shift_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    employee_id: int,
    shift_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        AddNoteModel,
        AddNoteModel,
    ],
) -> Response[Any]:
    """Add Note to Shift

     Adds a note to an existing shift.

    Args:
        employee_id (int):
        shift_id (int):
        body (AddNoteModel):
        body (AddNoteModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        employee_id=employee_id,
        shift_id=shift_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
