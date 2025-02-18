from enum import Enum


class EmployerRecurringLiabilityModelExternalService(str, Enum):
    ABRIDGEDFILEIMPORT = "AbridgedFileImport"
    ACCESSFINANCIALS = "AccessFinancials"
    ACTIVECAMPAIGN = "ActiveCampaign"
    ADMIN = "Admin"
    AKAHU = "Akahu"
    API = "API"
    ATTACHE = "Attache"
    AUTOMATEDPUBLICHOLIDAYNOTWORKED = "AutomatedPublicHolidayNotWorked"
    AWARDSTORE = "AwardStore"
    BEAM = "Beam"
    BUREAUDASHBOARD = "BureauDashboard"
    BUSINESSCENTRAL = "BusinessCentral"
    CAXTON = "Caxton"
    CLICKSUPER = "ClickSuper"
    COMMA = "Comma"
    DEPUTY = "Deputy"
    DETAILEDFILEEXPORT = "DetailedFileExport"
    EMPLOYEEADVANCEDHOURSUPLOAD = "EmployeeAdvancedHoursUpload"
    EMPLOYEEPAYRATESUPLOAD = "EmployeePayRatesUpload"
    EMPLOYEEPORTAL = "EmployeePortal"
    EMPLOYEETIMEPUNCH = "EmployeeTimePunch"
    FILEEXPORT = "FileExport"
    FILEIMPORT = "FileImport"
    FINANCIALSOFFICE = "FinancialsOffice"
    FLATFILEEMPLOYEEIMPORTER = "FlatFileEmployeeImporter"
    FPSFILEIMPORTER = "FPSFileImporter"
    FREEAGENT = "FreeAgent"
    FRESHBOOKS = "FreshBooks"
    HARMONY = "Harmony"
    HMRCDPSPOSTGRADLOAN = "HmrcDpsPostGradLoan"
    HMRCDPSSTUDENTLOAN = "HmrcDpsStudentLoan"
    HMRCDPSUPDATE = "HmrcDpsUpdate"
    IMPORTEMPLOYEESELFSETUP = "ImportEmployeeSelfSetup"
    INSTAPAY = "InstaPay"
    INSTAPAYDAILY = "InstaPayDaily"
    INTEGRATEDROSTERING = "IntegratedRostering"
    INTEGRATEDTIMESHEETS = "IntegratedTimesheets"
    JONASPREMIER = "JonasPremier"
    KOUNTA = "Kounta"
    MAESTRANO = "Maestrano"
    MICROPOWER = "MicroPower"
    MYOB = "MYOB"
    NETSUITE = "NetSuite"
    NETSUITEONEWORLD = "NetSuiteOneWorld"
    NONE = "None"
    OAUTH = "OAuth"
    ONBOARDING = "Onboarding"
    PAYRUNAUTOMATION = "PayRunAutomation"
    PAYRUNDEFAULT = "PayRunDefault"
    PAYTRON = "Paytron"
    PENSIONSYNC = "PensionSync"
    PRONTOXI = "ProntoXI"
    QBOFORCEDMIGRATION = "QBOForcedMigration"
    QBOMIGRATIONTOOL = "QBOMigrationTool"
    QUICKBOOKS = "QuickBooks"
    QUICKBOOKSSTANDALONEPAYROLL = "QuickbooksStandalonePayroll"
    QUICKFILE = "Quickfile"
    RECKONACCOUNTS = "ReckonAccounts"
    ROSTERLIVE = "RosterLive"
    ROSTERTEMPLATE = "RosterTemplate"
    SAASU = "Saasu"
    SAGE50 = "Sage50"
    SAGE50FILEIMPORTER = "Sage50FileImporter"
    SAGEACCOUNTING = "SageAccounting"
    SAGEINTACCT = "SageIntacct"
    SALESFORCE = "Salesforce"
    SLACK = "Slack"
    SQUARE = "Square"
    STANDARDWORKDAY = "StandardWorkDay"
    STAPLEDSUPERFUND = "StapledSuperFund"
    STARFILEIMPORTER = "StarFileImporter"
    SUMMARYANDDETAILSEXPORT = "SummaryAndDetailsExport"
    SWAG = "Swag"
    TELLEROO = "Telleroo"
    TIDE = "Tide"
    TIDESSO = "TideSso"
    TIMEANDATTENDANCEKIOSK = "TimeAndAttendanceKiosk"
    TWINFIELD = "Twinfield"
    WAGEEASY = "WageEasy"
    WIISE = "Wiise"
    WORKZONE = "WorkZone"
    WORKZONECLOCKONOFF = "WorkZoneClockOnOff"
    XERO = "Xero"
    XEROIDENTITYHRSIGNUP = "XeroIdentityHrSignUp"
    XEROIDENTITYPAYROLLSIGNUP = "XeroIdentityPayrollSignUp"
    ZAPIER = "Zapier"
    ZEPTO = "Zepto"
    ZOHO = "Zoho"

    def __str__(self) -> str:
        return str(self.value)
