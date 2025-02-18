from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NetToGrossRequest")


@_attrs_define
class NetToGrossRequest:
    """
    Attributes:
        net_amount (Union[Unset, float]):
        pay_category_id (Union[Unset, int]):
        pay_run_total_id (Union[Unset, int]):
    """

    net_amount: Union[Unset, float] = UNSET
    pay_category_id: Union[Unset, int] = UNSET
    pay_run_total_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        net_amount = self.net_amount

        pay_category_id = self.pay_category_id

        pay_run_total_id = self.pay_run_total_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if net_amount is not UNSET:
            field_dict["netAmount"] = net_amount
        if pay_category_id is not UNSET:
            field_dict["payCategoryId"] = pay_category_id
        if pay_run_total_id is not UNSET:
            field_dict["payRunTotalId"] = pay_run_total_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        net_amount = d.pop("netAmount", UNSET)

        pay_category_id = d.pop("payCategoryId", UNSET)

        pay_run_total_id = d.pop("payRunTotalId", UNSET)

        net_to_gross_request = cls(
            net_amount=net_amount,
            pay_category_id=pay_category_id,
            pay_run_total_id=pay_run_total_id,
        )

        net_to_gross_request.additional_properties = d
        return net_to_gross_request

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
