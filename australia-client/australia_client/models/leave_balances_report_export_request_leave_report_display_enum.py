from enum import Enum


class LeaveBalancesReportExportRequestLeaveReportDisplayEnum(str, Enum):
    ACCRUALLOCATION = "AccrualLocation"
    DEFAULTLOCATION = "DefaultLocation"

    def __str__(self) -> str:
        return str(self.value)
