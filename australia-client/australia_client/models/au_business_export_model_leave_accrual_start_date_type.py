from enum import Enum


class AuBusinessExportModelLeaveAccrualStartDateType(str, Enum):
    CALENDARYEAR = "CalendarYear"
    CATEGORYSPECIFICDATE = "CategorySpecificDate"
    EMPLOYEESTARTDATE = "EmployeeStartDate"
    SPECIFIEDDATE = "SpecifiedDate"

    def __str__(self) -> str:
        return str(self.value)
