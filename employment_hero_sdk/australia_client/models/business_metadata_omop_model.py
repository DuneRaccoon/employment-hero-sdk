from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BusinessMetadataOmopModel")


@_attrs_define
class BusinessMetadataOmopModel:
    """
    Attributes:
        id (Union[Unset, int]):
        mdm_id (Union[Unset, str]):
    """

    id: Union[Unset, int] = UNSET
    mdm_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        mdm_id = self.mdm_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if mdm_id is not UNSET:
            field_dict["mdmId"] = mdm_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id", UNSET)

        mdm_id = d.pop("mdmId", UNSET)

        business_metadata_omop_model = cls(
            id=id,
            mdm_id=mdm_id,
        )

        business_metadata_omop_model.additional_properties = d
        return business_metadata_omop_model

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
