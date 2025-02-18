from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.ess_leave_upload_i_http_action_result import EssLeaveUploadIHttpActionResult
from ...types import Response


def _get_kwargs(
    employee_id: str,
    leave_request_id: int,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": f"/api/v2/ess/{employee_id}/leave/{leave_request_id}/attachment",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[EssLeaveUploadIHttpActionResult]:
    if response.status_code == HTTPStatus.OK:
        response_200 = EssLeaveUploadIHttpActionResult.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[EssLeaveUploadIHttpActionResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    employee_id: str,
    leave_request_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[EssLeaveUploadIHttpActionResult]:
    """Upload Attachment to Leave Request

     Uploads a file as a new employee document, and attaches it to the leave request with the specified
    ID.
    The request should be a MIME multipart file upload request.

    Args:
        employee_id (str):
        leave_request_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EssLeaveUploadIHttpActionResult]
    """

    kwargs = _get_kwargs(
        employee_id=employee_id,
        leave_request_id=leave_request_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    employee_id: str,
    leave_request_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[EssLeaveUploadIHttpActionResult]:
    """Upload Attachment to Leave Request

     Uploads a file as a new employee document, and attaches it to the leave request with the specified
    ID.
    The request should be a MIME multipart file upload request.

    Args:
        employee_id (str):
        leave_request_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EssLeaveUploadIHttpActionResult
    """

    return sync_detailed(
        employee_id=employee_id,
        leave_request_id=leave_request_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    employee_id: str,
    leave_request_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[EssLeaveUploadIHttpActionResult]:
    """Upload Attachment to Leave Request

     Uploads a file as a new employee document, and attaches it to the leave request with the specified
    ID.
    The request should be a MIME multipart file upload request.

    Args:
        employee_id (str):
        leave_request_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EssLeaveUploadIHttpActionResult]
    """

    kwargs = _get_kwargs(
        employee_id=employee_id,
        leave_request_id=leave_request_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    employee_id: str,
    leave_request_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[EssLeaveUploadIHttpActionResult]:
    """Upload Attachment to Leave Request

     Uploads a file as a new employee document, and attaches it to the leave request with the specified
    ID.
    The request should be a MIME multipart file upload request.

    Args:
        employee_id (str):
        leave_request_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EssLeaveUploadIHttpActionResult
    """

    return (
        await asyncio_detailed(
            employee_id=employee_id,
            leave_request_id=leave_request_id,
            client=client,
        )
    ).parsed
