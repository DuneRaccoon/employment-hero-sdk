from enum import Enum


class TimesheetReportRequestModelTimesheetLineStatusType(str, Enum):
    APPROVED = "Approved"
    MISSING = "Missing"
    PROCESSED = "Processed"
    REJECTED = "Rejected"
    SUBMITTED = "Submitted"

    def __str__(self) -> str:
        return str(self.value)
