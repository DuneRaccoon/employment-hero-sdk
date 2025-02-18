from enum import Enum


class TimesheetRequestFilterModelNullableTimesheetGrouping(str, Enum):
    DATE = "Date"
    DEFAULTLOCATION = "DefaultLocation"
    EMPLOYEE = "Employee"
    LOCATION = "Location"
    PAYSCHEDULE = "PaySchedule"
    WORKTYPE = "WorkType"

    def __str__(self) -> str:
        return str(self.value)
