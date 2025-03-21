from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PayRunSuperBatchModel")


@_attrs_define
class PayRunSuperBatchModel:
    """
    Attributes:
        super_interchange_id (Union[Unset, int]):
        description (Union[Unset, str]):
    """

    super_interchange_id: Union[Unset, int] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        super_interchange_id = self.super_interchange_id

        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if super_interchange_id is not UNSET:
            field_dict["superInterchangeId"] = super_interchange_id
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        super_interchange_id = d.pop("superInterchangeId", UNSET)

        description = d.pop("description", UNSET)

        pay_run_super_batch_model = cls(
            super_interchange_id=super_interchange_id,
            description=description,
        )

        pay_run_super_batch_model.additional_properties = d
        return pay_run_super_batch_model

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
