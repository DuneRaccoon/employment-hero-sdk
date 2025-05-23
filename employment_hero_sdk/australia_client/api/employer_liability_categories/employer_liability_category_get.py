from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.employer_liability_category_model import EmployerLiabilityCategoryModel
from ...types import Response


def _get_kwargs(
    business_id: str,
    id: int,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/api/v2/business/{business_id}/employerliabilitycategory/{id}",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[EmployerLiabilityCategoryModel]:
    if response.status_code == HTTPStatus.OK:
        response_200 = EmployerLiabilityCategoryModel.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[EmployerLiabilityCategoryModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    business_id: str,
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[EmployerLiabilityCategoryModel]:
    """Get Employer Liability Category

     Gets the employer liability category with the specified ID.

    Args:
        business_id (str):
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EmployerLiabilityCategoryModel]
    """

    kwargs = _get_kwargs(
        business_id=business_id,
        id=id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    business_id: str,
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[EmployerLiabilityCategoryModel]:
    """Get Employer Liability Category

     Gets the employer liability category with the specified ID.

    Args:
        business_id (str):
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EmployerLiabilityCategoryModel
    """

    return sync_detailed(
        business_id=business_id,
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    business_id: str,
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[EmployerLiabilityCategoryModel]:
    """Get Employer Liability Category

     Gets the employer liability category with the specified ID.

    Args:
        business_id (str):
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[EmployerLiabilityCategoryModel]
    """

    kwargs = _get_kwargs(
        business_id=business_id,
        id=id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    business_id: str,
    id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[EmployerLiabilityCategoryModel]:
    """Get Employer Liability Category

     Gets the employer liability category with the specified ID.

    Args:
        business_id (str):
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        EmployerLiabilityCategoryModel
    """

    return (
        await asyncio_detailed(
            business_id=business_id,
            id=id,
            client=client,
        )
    ).parsed
