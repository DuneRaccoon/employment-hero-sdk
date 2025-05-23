from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.au_ess_bank_account_model import AuEssBankAccountModel
from ...types import Response


def _get_kwargs(
    employee_id: str,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/api/v2/ess/{employee_id}/bankaccounts/swagrequired2fa",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[List["AuEssBankAccountModel"]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = AuEssBankAccountModel.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[List["AuEssBankAccountModel"]]:
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
) -> Response[List["AuEssBankAccountModel"]]:
    """List Bank Accounts

     Lists all of the bank accounts for this employee.

    Args:
        employee_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['AuEssBankAccountModel']]
    """

    kwargs = _get_kwargs(
        employee_id=employee_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    employee_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[List["AuEssBankAccountModel"]]:
    """List Bank Accounts

     Lists all of the bank accounts for this employee.

    Args:
        employee_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['AuEssBankAccountModel']
    """

    return sync_detailed(
        employee_id=employee_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    employee_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[List["AuEssBankAccountModel"]]:
    """List Bank Accounts

     Lists all of the bank accounts for this employee.

    Args:
        employee_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['AuEssBankAccountModel']]
    """

    kwargs = _get_kwargs(
        employee_id=employee_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    employee_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[List["AuEssBankAccountModel"]]:
    """List Bank Accounts

     Lists all of the bank accounts for this employee.

    Args:
        employee_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['AuEssBankAccountModel']
    """

    return (
        await asyncio_detailed(
            employee_id=employee_id,
            client=client,
        )
    ).parsed
