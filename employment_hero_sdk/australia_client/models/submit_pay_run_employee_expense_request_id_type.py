from enum import Enum


class SubmitPayRunEmployeeExpenseRequestIdType(str, Enum):
    EXTERNAL = "External"
    STANDARD = "Standard"

    def __str__(self) -> str:
        return str(self.value)
