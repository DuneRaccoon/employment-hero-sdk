from enum import Enum


class AuReportsSuperContributionsGetExcelReportRequestContributionType(str, Enum):
    EMPLOYERCONTRIBUTION = "EmployerContribution"
    MEMBERVOLUNTARY = "MemberVoluntary"
    NONRESCEMPLOYERCONTRIBUTION = "NonRescEmployerContribution"
    SALARYSACRIFICE = "SalarySacrifice"
    SUPERGUARANTEE = "SuperGuarantee"

    def __str__(self) -> str:
        return str(self.value)
