from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.au_bank_payment_model import AuBankPaymentModel
from ...types import Response


def _get_kwargs(
    business_id: str,
    pay_run_id: int,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/api/v2/business/{business_id}/payrun/{pay_run_id}/payments",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[List["AuBankPaymentModel"]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = AuBankPaymentModel.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[List["AuBankPaymentModel"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    business_id: str,
    pay_run_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[List["AuBankPaymentModel"]]:
    """Get pay run payments

     Gets the payments associated with a pay run.

    Args:
        business_id (str):
        pay_run_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['AuBankPaymentModel']]
    """

    kwargs = _get_kwargs(
        business_id=business_id,
        pay_run_id=pay_run_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    business_id: str,
    pay_run_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[List["AuBankPaymentModel"]]:
    """Get pay run payments

     Gets the payments associated with a pay run.

    Args:
        business_id (str):
        pay_run_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['AuBankPaymentModel']
    """

    return sync_detailed(
        business_id=business_id,
        pay_run_id=pay_run_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    business_id: str,
    pay_run_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[List["AuBankPaymentModel"]]:
    """Get pay run payments

     Gets the payments associated with a pay run.

    Args:
        business_id (str):
        pay_run_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['AuBankPaymentModel']]
    """

    kwargs = _get_kwargs(
        business_id=business_id,
        pay_run_id=pay_run_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    business_id: str,
    pay_run_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[List["AuBankPaymentModel"]]:
    """Get pay run payments

     Gets the payments associated with a pay run.

    Args:
        business_id (str):
        pay_run_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['AuBankPaymentModel']
    """

    return (
        await asyncio_detailed(
            business_id=business_id,
            pay_run_id=pay_run_id,
            client=client,
        )
    ).parsed
