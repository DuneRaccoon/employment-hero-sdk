from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.pay_rate_template_pay_category_export_model import PayRateTemplatePayCategoryExportModel


T = TypeVar("T", bound="AuPayRateTemplateModel")


@_attrs_define
class AuPayRateTemplateModel:
    """
    Attributes:
        super_threshold_amount (Union[Unset, float]):
        maximum_quarterly_super_contributions_base (Union[Unset, float]):
        id (Union[Unset, int]):
        name (Union[Unset, str]):
        primary_pay_category_id (Union[Unset, int]):
        pay_categories (Union[Unset, List['PayRateTemplatePayCategoryExportModel']]):
        external_id (Union[Unset, str]):
        source (Union[Unset, str]):
        reapply_to_linked_employees (Union[Unset, bool]):
    """

    super_threshold_amount: Union[Unset, float] = UNSET
    maximum_quarterly_super_contributions_base: Union[Unset, float] = UNSET
    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    primary_pay_category_id: Union[Unset, int] = UNSET
    pay_categories: Union[Unset, List["PayRateTemplatePayCategoryExportModel"]] = UNSET
    external_id: Union[Unset, str] = UNSET
    source: Union[Unset, str] = UNSET
    reapply_to_linked_employees: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        super_threshold_amount = self.super_threshold_amount

        maximum_quarterly_super_contributions_base = self.maximum_quarterly_super_contributions_base

        id = self.id

        name = self.name

        primary_pay_category_id = self.primary_pay_category_id

        pay_categories: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.pay_categories, Unset):
            pay_categories = []
            for pay_categories_item_data in self.pay_categories:
                pay_categories_item = pay_categories_item_data.to_dict()
                pay_categories.append(pay_categories_item)

        external_id = self.external_id

        source = self.source

        reapply_to_linked_employees = self.reapply_to_linked_employees

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if super_threshold_amount is not UNSET:
            field_dict["superThresholdAmount"] = super_threshold_amount
        if maximum_quarterly_super_contributions_base is not UNSET:
            field_dict["maximumQuarterlySuperContributionsBase"] = maximum_quarterly_super_contributions_base
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if primary_pay_category_id is not UNSET:
            field_dict["primaryPayCategoryId"] = primary_pay_category_id
        if pay_categories is not UNSET:
            field_dict["payCategories"] = pay_categories
        if external_id is not UNSET:
            field_dict["externalId"] = external_id
        if source is not UNSET:
            field_dict["source"] = source
        if reapply_to_linked_employees is not UNSET:
            field_dict["reapplyToLinkedEmployees"] = reapply_to_linked_employees

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.pay_rate_template_pay_category_export_model import PayRateTemplatePayCategoryExportModel

        d = src_dict.copy()
        super_threshold_amount = d.pop("superThresholdAmount", UNSET)

        maximum_quarterly_super_contributions_base = d.pop("maximumQuarterlySuperContributionsBase", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        primary_pay_category_id = d.pop("primaryPayCategoryId", UNSET)

        pay_categories = []
        _pay_categories = d.pop("payCategories", UNSET)
        for pay_categories_item_data in _pay_categories or []:
            pay_categories_item = PayRateTemplatePayCategoryExportModel.from_dict(pay_categories_item_data)

            pay_categories.append(pay_categories_item)

        external_id = d.pop("externalId", UNSET)

        source = d.pop("source", UNSET)

        reapply_to_linked_employees = d.pop("reapplyToLinkedEmployees", UNSET)

        au_pay_rate_template_model = cls(
            super_threshold_amount=super_threshold_amount,
            maximum_quarterly_super_contributions_base=maximum_quarterly_super_contributions_base,
            id=id,
            name=name,
            primary_pay_category_id=primary_pay_category_id,
            pay_categories=pay_categories,
            external_id=external_id,
            source=source,
            reapply_to_linked_employees=reapply_to_linked_employees,
        )

        au_pay_rate_template_model.additional_properties = d
        return au_pay_rate_template_model

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
