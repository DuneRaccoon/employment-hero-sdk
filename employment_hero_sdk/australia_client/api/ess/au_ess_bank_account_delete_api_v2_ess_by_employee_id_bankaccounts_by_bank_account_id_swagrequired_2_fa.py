from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.au_ess_save_bank_account_response_model import AuEssSaveBankAccountResponseModel
from ...types import Response


def _get_kwargs(
    employee_id: str,
    bank_account_id: int,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "delete",
        "url": f"/api/v2/ess/{employee_id}/bankaccounts/{bank_account_id}/swagrequired2fa",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[AuEssSaveBankAccountResponseModel]:
    if response.status_code == HTTPStatus.OK:
        response_200 = AuEssSaveBankAccountResponseModel.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[AuEssSaveBankAccountResponseModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    employee_id: str,
    bank_account_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[AuEssSaveBankAccountResponseModel]:
    """Delete Bank Account

     Deletes the employee's bank account with the specified ID.

    Args:
        employee_id (str):
        bank_account_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AuEssSaveBankAccountResponseModel]
    """

    kwargs = _get_kwargs(
        employee_id=employee_id,
        bank_account_id=bank_account_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    employee_id: str,
    bank_account_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[AuEssSaveBankAccountResponseModel]:
    """Delete Bank Account

     Deletes the employee's bank account with the specified ID.

    Args:
        employee_id (str):
        bank_account_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AuEssSaveBankAccountResponseModel
    """

    return sync_detailed(
        employee_id=employee_id,
        bank_account_id=bank_account_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    employee_id: str,
    bank_account_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[AuEssSaveBankAccountResponseModel]:
    """Delete Bank Account

     Deletes the employee's bank account with the specified ID.

    Args:
        employee_id (str):
        bank_account_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AuEssSaveBankAccountResponseModel]
    """

    kwargs = _get_kwargs(
        employee_id=employee_id,
        bank_account_id=bank_account_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    employee_id: str,
    bank_account_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[AuEssSaveBankAccountResponseModel]:
    """Delete Bank Account

     Deletes the employee's bank account with the specified ID.

    Args:
        employee_id (str):
        bank_account_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AuEssSaveBankAccountResponseModel
    """

    return (
        await asyncio_detailed(
            employee_id=employee_id,
            bank_account_id=bank_account_id,
            client=client,
        )
    ).parsed
