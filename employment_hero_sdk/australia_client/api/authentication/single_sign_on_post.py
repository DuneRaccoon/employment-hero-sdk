from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.single_sign_on_request_model import SingleSignOnRequestModel
from ...models.single_sign_on_response_model import SingleSignOnResponseModel
from ...types import Response


def _get_kwargs(
    *,
    body: Union[
        SingleSignOnRequestModel,
        SingleSignOnRequestModel,
    ],
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/api/v2/singlesignon",
    }

    if isinstance(body, SingleSignOnRequestModel):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, SingleSignOnRequestModel):
        _data_body = body.to_dict()

        _kwargs["data"] = _data_body
        headers["Content-Type"] = "application/x-www-form-urlencoded"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[SingleSignOnResponseModel]:
    if response.status_code == HTTPStatus.OK:
        response_200 = SingleSignOnResponseModel.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[SingleSignOnResponseModel]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        SingleSignOnRequestModel,
        SingleSignOnRequestModel,
    ],
) -> Response[SingleSignOnResponseModel]:
    r"""Single Sign On

     Request for SSO URL that provides authenticated access to KeyPay. See the guide on <a
    href=\"http://api.keypay.com.au/guides/SSO\">SSO Requests</a> for more details.

    Args:
        body (SingleSignOnRequestModel):
        body (SingleSignOnRequestModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SingleSignOnResponseModel]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        SingleSignOnRequestModel,
        SingleSignOnRequestModel,
    ],
) -> Optional[SingleSignOnResponseModel]:
    r"""Single Sign On

     Request for SSO URL that provides authenticated access to KeyPay. See the guide on <a
    href=\"http://api.keypay.com.au/guides/SSO\">SSO Requests</a> for more details.

    Args:
        body (SingleSignOnRequestModel):
        body (SingleSignOnRequestModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SingleSignOnResponseModel
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        SingleSignOnRequestModel,
        SingleSignOnRequestModel,
    ],
) -> Response[SingleSignOnResponseModel]:
    r"""Single Sign On

     Request for SSO URL that provides authenticated access to KeyPay. See the guide on <a
    href=\"http://api.keypay.com.au/guides/SSO\">SSO Requests</a> for more details.

    Args:
        body (SingleSignOnRequestModel):
        body (SingleSignOnRequestModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[SingleSignOnResponseModel]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: Union[
        SingleSignOnRequestModel,
        SingleSignOnRequestModel,
    ],
) -> Optional[SingleSignOnResponseModel]:
    r"""Single Sign On

     Request for SSO URL that provides authenticated access to KeyPay. See the guide on <a
    href=\"http://api.keypay.com.au/guides/SSO\">SSO Requests</a> for more details.

    Args:
        body (SingleSignOnRequestModel):
        body (SingleSignOnRequestModel):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        SingleSignOnResponseModel
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
