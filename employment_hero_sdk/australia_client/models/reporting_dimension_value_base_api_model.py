from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReportingDimensionValueBaseApiModel")


@_attrs_define
class ReportingDimensionValueBaseApiModel:
    """
    Attributes:
        id (Union[Unset, int]):
        name (Union[Unset, str]):
        reporting_dimension_id (Union[Unset, int]):
    """

    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    reporting_dimension_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        name = self.name

        reporting_dimension_id = self.reporting_dimension_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if reporting_dimension_id is not UNSET:
            field_dict["reportingDimensionId"] = reporting_dimension_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        reporting_dimension_id = d.pop("reportingDimensionId", UNSET)

        reporting_dimension_value_base_api_model = cls(
            id=id,
            name=name,
            reporting_dimension_id=reporting_dimension_id,
        )

        reporting_dimension_value_base_api_model.additional_properties = d
        return reporting_dimension_value_base_api_model

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
