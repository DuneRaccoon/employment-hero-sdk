from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.employee_document_model import EmployeeDocumentModel
from ...types import Response


def _get_kwargs(
    business_id: str,
    employee_id: str,
    id: int,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/api/v2/business/{business_id}/employee/{employee_id}/document/{id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[EmployeeDocumentModel]:
    if response.status_code == HTTPStatus.OK:
        response_200 = EmployeeDocumentModel.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[EmployeeDocumentModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    business_id: str,
    employee_id: str,
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[EmployeeDocumentModel]:
    """Get Employee Document Details

     Gets the details for the employee document with the specified ID.

    Args:
        business_id (str):
        employee_id (str):
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EmployeeDocumentModel]
    """

    kwargs = _get_kwargs(
        business_id=business_id,
        employee_id=employee_id,
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    business_id: str,
    employee_id: str,
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[EmployeeDocumentModel]:
    """Get Employee Document Details

     Gets the details for the employee document with the specified ID.

    Args:
        business_id (str):
        employee_id (str):
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EmployeeDocumentModel
    """

    return sync_detailed(
        business_id=business_id,
        employee_id=employee_id,
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    business_id: str,
    employee_id: str,
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[EmployeeDocumentModel]:
    """Get Employee Document Details

     Gets the details for the employee document with the specified ID.

    Args:
        business_id (str):
        employee_id (str):
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EmployeeDocumentModel]
    """

    kwargs = _get_kwargs(
        business_id=business_id,
        employee_id=employee_id,
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    business_id: str,
    employee_id: str,
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[EmployeeDocumentModel]:
    """Get Employee Document Details

     Gets the details for the employee document with the specified ID.

    Args:
        business_id (str):
        employee_id (str):
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EmployeeDocumentModel
    """

    return (
        await asyncio_detailed(
            business_id=business_id,
            employee_id=employee_id,
            id=id,
            client=client,
        )
    ).parsed
