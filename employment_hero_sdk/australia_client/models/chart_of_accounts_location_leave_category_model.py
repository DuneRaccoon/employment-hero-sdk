from typing import Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ChartOfAccountsLocationLeaveCategoryModel")


@_attrs_define
class ChartOfAccountsLocationLeaveCategoryModel:
    """
    Attributes:
        liability_account_id (Union[Unset, int]):
        accrue_from_contingent_period (Union[Unset, bool]):
        id (Union[Unset, int]):
        name (Union[Unset, str]):
        expense_account_id (Union[Unset, int]):
    """

    liability_account_id: Union[Unset, int] = UNSET
    accrue_from_contingent_period: Union[Unset, bool] = UNSET
    id: Union[Unset, int] = UNSET
    name: Union[Unset, str] = UNSET
    expense_account_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        liability_account_id = self.liability_account_id

        accrue_from_contingent_period = self.accrue_from_contingent_period

        id = self.id

        name = self.name

        expense_account_id = self.expense_account_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if liability_account_id is not UNSET:
            field_dict["liabilityAccountId"] = liability_account_id
        if accrue_from_contingent_period is not UNSET:
            field_dict["accrueFromContingentPeriod"] = accrue_from_contingent_period
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if expense_account_id is not UNSET:
            field_dict["expenseAccountId"] = expense_account_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        liability_account_id = d.pop("liabilityAccountId", UNSET)

        accrue_from_contingent_period = d.pop("accrueFromContingentPeriod", UNSET)

        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        expense_account_id = d.pop("expenseAccountId", UNSET)

        chart_of_accounts_location_leave_category_model = cls(
            liability_account_id=liability_account_id,
            accrue_from_contingent_period=accrue_from_contingent_period,
            id=id,
            name=name,
            expense_account_id=expense_account_id,
        )

        chart_of_accounts_location_leave_category_model.additional_properties = d
        return chart_of_accounts_location_leave_category_model

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
