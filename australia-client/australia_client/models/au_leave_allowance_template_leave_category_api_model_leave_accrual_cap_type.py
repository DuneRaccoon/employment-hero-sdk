from enum import Enum


class AuLeaveAllowanceTemplateLeaveCategoryApiModelLeaveAccrualCapType(str, Enum):
    LIMITED = "Limited"
    NOTLIMITED = "NotLimited"

    def __str__(self) -> str:
        return str(self.value)
