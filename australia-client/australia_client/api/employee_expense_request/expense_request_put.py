from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.expense_request_edit_model import ExpenseRequestEditModel
from ...types import Response


def _get_kwargs(
    business_id: str,
    employee_id: str,
    expense_request_id: int,
    *,
    body: Union[
        ExpenseRequestEditModel,
        ExpenseRequestEditModel,
    ],
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "put",
        "url": f"/api/v2/business/{business_id}/employee/{employee_id}/expenserequest/{expense_request_id}",
    }

    if isinstance(body, ExpenseRequestEditModel):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, ExpenseRequestEditModel):
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
    expense_request_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        ExpenseRequestEditModel,
        ExpenseRequestEditModel,
    ],
) -> Response[Any]:
    """Update Expense Request

     Updates the expense request with the specified ID.

    Args:
        business_id (str):
        employee_id (str):
        expense_request_id (int):
        body (ExpenseRequestEditModel):
        body (ExpenseRequestEditModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        business_id=business_id,
        employee_id=employee_id,
        expense_request_id=expense_request_id,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    business_id: str,
    employee_id: str,
    expense_request_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        ExpenseRequestEditModel,
        ExpenseRequestEditModel,
    ],
) -> Response[Any]:
    """Update Expense Request

     Updates the expense request with the specified ID.

    Args:
        business_id (str):
        employee_id (str):
        expense_request_id (int):
        body (ExpenseRequestEditModel):
        body (ExpenseRequestEditModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        business_id=business_id,
        employee_id=employee_id,
        expense_request_id=expense_request_id,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
