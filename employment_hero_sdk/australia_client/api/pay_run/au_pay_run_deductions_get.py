from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.au_pay_run_deduction_response import AuPayRunDeductionResponse
from ...types import Response


def _get_kwargs(
    business_id: str,
    pay_run_id: int,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/api/v2/business/{business_id}/payrun/{pay_run_id}/deductions",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[AuPayRunDeductionResponse]:
    if response.status_code == HTTPStatus.OK:
        response_200 = AuPayRunDeductionResponse.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[AuPayRunDeductionResponse]:
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
) -> Response[AuPayRunDeductionResponse]:
    """List Deductions

     Gets all the deductions for a pay run.

    Args:
        business_id (str):
        pay_run_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AuPayRunDeductionResponse]
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
) -> Optional[AuPayRunDeductionResponse]:
    """List Deductions

     Gets all the deductions for a pay run.

    Args:
        business_id (str):
        pay_run_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AuPayRunDeductionResponse
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
) -> Response[AuPayRunDeductionResponse]:
    """List Deductions

     Gets all the deductions for a pay run.

    Args:
        business_id (str):
        pay_run_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[AuPayRunDeductionResponse]
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
) -> Optional[AuPayRunDeductionResponse]:
    """List Deductions

     Gets all the deductions for a pay run.

    Args:
        business_id (str):
        pay_run_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        AuPayRunDeductionResponse
    """

    return (
        await asyncio_detailed(
            business_id=business_id,
            pay_run_id=pay_run_id,
            client=client,
        )
    ).parsed
