import datetime
from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.reports_shift_swapping_get_roster_shift_swap_status_enum import (
    ReportsShiftSwappingGetRosterShiftSwapStatusEnum,
)
from ...models.shift_swapping_report_export_model import ShiftSwappingReportExportModel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    business_id: str,
    *,
    request_from_employee_id: Union[Unset, int] = UNSET,
    request_to_employee_id: Union[Unset, int] = UNSET,
    request_include_costs: Union[Unset, bool] = UNSET,
    request_statuses: Union[Unset, List[ReportsShiftSwappingGetRosterShiftSwapStatusEnum]] = UNSET,
    request_from_date: Union[Unset, datetime.datetime] = UNSET,
    request_to_date: Union[Unset, datetime.datetime] = UNSET,
    request_location_id: Union[Unset, int] = UNSET,
    request_employing_entity_id: Union[Unset, int] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["request.fromEmployeeId"] = request_from_employee_id

    params["request.toEmployeeId"] = request_to_employee_id

    params["request.includeCosts"] = request_include_costs

    json_request_statuses: Union[Unset, List[str]] = UNSET
    if not isinstance(request_statuses, Unset):
        json_request_statuses = []
        for request_statuses_item_data in request_statuses:
            request_statuses_item = request_statuses_item_data.value
            json_request_statuses.append(request_statuses_item)

    params["request.statuses"] = json_request_statuses

    json_request_from_date: Union[Unset, str] = UNSET
    if not isinstance(request_from_date, Unset):
        json_request_from_date = request_from_date.isoformat()
    params["request.fromDate"] = json_request_from_date

    json_request_to_date: Union[Unset, str] = UNSET
    if not isinstance(request_to_date, Unset):
        json_request_to_date = request_to_date.isoformat()
    params["request.toDate"] = json_request_to_date

    params["request.locationId"] = request_location_id

    params["request.employingEntityId"] = request_employing_entity_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": f"/api/v2/business/{business_id}/report/shiftswapping",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[List["ShiftSwappingReportExportModel"]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ShiftSwappingReportExportModel.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[List["ShiftSwappingReportExportModel"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    business_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    request_from_employee_id: Union[Unset, int] = UNSET,
    request_to_employee_id: Union[Unset, int] = UNSET,
    request_include_costs: Union[Unset, bool] = UNSET,
    request_statuses: Union[Unset, List[ReportsShiftSwappingGetRosterShiftSwapStatusEnum]] = UNSET,
    request_from_date: Union[Unset, datetime.datetime] = UNSET,
    request_to_date: Union[Unset, datetime.datetime] = UNSET,
    request_location_id: Union[Unset, int] = UNSET,
    request_employing_entity_id: Union[Unset, int] = UNSET,
) -> Response[List["ShiftSwappingReportExportModel"]]:
    """Get shift swapping report by business id

    Args:
        business_id (str):
        request_from_employee_id (Union[Unset, int]):
        request_to_employee_id (Union[Unset, int]):
        request_include_costs (Union[Unset, bool]):
        request_statuses (Union[Unset, List[ReportsShiftSwappingGetRosterShiftSwapStatusEnum]]):
        request_from_date (Union[Unset, datetime.datetime]):
        request_to_date (Union[Unset, datetime.datetime]):
        request_location_id (Union[Unset, int]):
        request_employing_entity_id (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['ShiftSwappingReportExportModel']]
    """

    kwargs = _get_kwargs(
        business_id=business_id,
        request_from_employee_id=request_from_employee_id,
        request_to_employee_id=request_to_employee_id,
        request_include_costs=request_include_costs,
        request_statuses=request_statuses,
        request_from_date=request_from_date,
        request_to_date=request_to_date,
        request_location_id=request_location_id,
        request_employing_entity_id=request_employing_entity_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    business_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    request_from_employee_id: Union[Unset, int] = UNSET,
    request_to_employee_id: Union[Unset, int] = UNSET,
    request_include_costs: Union[Unset, bool] = UNSET,
    request_statuses: Union[Unset, List[ReportsShiftSwappingGetRosterShiftSwapStatusEnum]] = UNSET,
    request_from_date: Union[Unset, datetime.datetime] = UNSET,
    request_to_date: Union[Unset, datetime.datetime] = UNSET,
    request_location_id: Union[Unset, int] = UNSET,
    request_employing_entity_id: Union[Unset, int] = UNSET,
) -> Optional[List["ShiftSwappingReportExportModel"]]:
    """Get shift swapping report by business id

    Args:
        business_id (str):
        request_from_employee_id (Union[Unset, int]):
        request_to_employee_id (Union[Unset, int]):
        request_include_costs (Union[Unset, bool]):
        request_statuses (Union[Unset, List[ReportsShiftSwappingGetRosterShiftSwapStatusEnum]]):
        request_from_date (Union[Unset, datetime.datetime]):
        request_to_date (Union[Unset, datetime.datetime]):
        request_location_id (Union[Unset, int]):
        request_employing_entity_id (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['ShiftSwappingReportExportModel']
    """

    return sync_detailed(
        business_id=business_id,
        client=client,
        request_from_employee_id=request_from_employee_id,
        request_to_employee_id=request_to_employee_id,
        request_include_costs=request_include_costs,
        request_statuses=request_statuses,
        request_from_date=request_from_date,
        request_to_date=request_to_date,
        request_location_id=request_location_id,
        request_employing_entity_id=request_employing_entity_id,
    ).parsed


async def asyncio_detailed(
    business_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    request_from_employee_id: Union[Unset, int] = UNSET,
    request_to_employee_id: Union[Unset, int] = UNSET,
    request_include_costs: Union[Unset, bool] = UNSET,
    request_statuses: Union[Unset, List[ReportsShiftSwappingGetRosterShiftSwapStatusEnum]] = UNSET,
    request_from_date: Union[Unset, datetime.datetime] = UNSET,
    request_to_date: Union[Unset, datetime.datetime] = UNSET,
    request_location_id: Union[Unset, int] = UNSET,
    request_employing_entity_id: Union[Unset, int] = UNSET,
) -> Response[List["ShiftSwappingReportExportModel"]]:
    """Get shift swapping report by business id

    Args:
        business_id (str):
        request_from_employee_id (Union[Unset, int]):
        request_to_employee_id (Union[Unset, int]):
        request_include_costs (Union[Unset, bool]):
        request_statuses (Union[Unset, List[ReportsShiftSwappingGetRosterShiftSwapStatusEnum]]):
        request_from_date (Union[Unset, datetime.datetime]):
        request_to_date (Union[Unset, datetime.datetime]):
        request_location_id (Union[Unset, int]):
        request_employing_entity_id (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[List['ShiftSwappingReportExportModel']]
    """

    kwargs = _get_kwargs(
        business_id=business_id,
        request_from_employee_id=request_from_employee_id,
        request_to_employee_id=request_to_employee_id,
        request_include_costs=request_include_costs,
        request_statuses=request_statuses,
        request_from_date=request_from_date,
        request_to_date=request_to_date,
        request_location_id=request_location_id,
        request_employing_entity_id=request_employing_entity_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    business_id: str,
    *,
    client: Union[AuthenticatedClient, Client],
    request_from_employee_id: Union[Unset, int] = UNSET,
    request_to_employee_id: Union[Unset, int] = UNSET,
    request_include_costs: Union[Unset, bool] = UNSET,
    request_statuses: Union[Unset, List[ReportsShiftSwappingGetRosterShiftSwapStatusEnum]] = UNSET,
    request_from_date: Union[Unset, datetime.datetime] = UNSET,
    request_to_date: Union[Unset, datetime.datetime] = UNSET,
    request_location_id: Union[Unset, int] = UNSET,
    request_employing_entity_id: Union[Unset, int] = UNSET,
) -> Optional[List["ShiftSwappingReportExportModel"]]:
    """Get shift swapping report by business id

    Args:
        business_id (str):
        request_from_employee_id (Union[Unset, int]):
        request_to_employee_id (Union[Unset, int]):
        request_include_costs (Union[Unset, bool]):
        request_statuses (Union[Unset, List[ReportsShiftSwappingGetRosterShiftSwapStatusEnum]]):
        request_from_date (Union[Unset, datetime.datetime]):
        request_to_date (Union[Unset, datetime.datetime]):
        request_location_id (Union[Unset, int]):
        request_employing_entity_id (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        List['ShiftSwappingReportExportModel']
    """

    return (
        await asyncio_detailed(
            business_id=business_id,
            client=client,
            request_from_employee_id=request_from_employee_id,
            request_to_employee_id=request_to_employee_id,
            request_include_costs=request_include_costs,
            request_statuses=request_statuses,
            request_from_date=request_from_date,
            request_to_date=request_to_date,
            request_location_id=request_location_id,
            request_employing_entity_id=request_employing_entity_id,
        )
    ).parsed
