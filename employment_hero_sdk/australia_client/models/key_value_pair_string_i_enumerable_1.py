from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="KeyValuePairStringIEnumerable1")


@_attrs_define
class KeyValuePairStringIEnumerable1:
    """
    Attributes:
        key (Union[Unset, str]):
        value (Union[Unset, List[str]]):
    """

    key: Union[Unset, str] = UNSET
    value: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        key = self.key

        value: Union[Unset, List[str]] = UNSET
        if not isinstance(self.value, Unset):
            value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if key is not UNSET:
            field_dict["key"] = key
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        key = d.pop("key", UNSET)

        value = cast(List[str], d.pop("value", UNSET))

        key_value_pair_string_i_enumerable_1 = cls(
            key=key,
            value=value,
        )

        key_value_pair_string_i_enumerable_1.additional_properties = d
        return key_value_pair_string_i_enumerable_1

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
