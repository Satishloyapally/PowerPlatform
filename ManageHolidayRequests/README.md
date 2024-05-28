# Manage Holiday Requests
ManageHolidayRequests
├── PowerAutomate
│   └── manage_holiday_requests_flow.json
├── Dataverse
│   └── schema.json
├── PowerApps
│   └── [PowerApps Project Files]
├── PowerPages
│   └── index.html
├── JavaScript
│   └── validateLeaveDates.js
├── Python
│   └── submit_leave_request.py
├── PowerBI
│   └── leave_requests_report.py
└── README.md

# Manage Holiday Requests

This project automates the leave request and approval process using Microsoft Power Platform.

## Project Structure
- **PowerAutomate**: Contains the flow definition JSON file.
- **Dataverse**: Contains the schema for the Dataverse table.
- **PowerApps**: Contains Power Apps project files.
- **PowerPages**: Contains HTML files for Power Pages.
- **JavaScript**: Contains JavaScript code to enhance Power Apps.
- **Python**: Contains Python scripts for integration.
- **PowerBI**: Contains Python scripts to generate Power BI reports.

- Manage Holiday Requests
Power Automate Flow:

Use Case: Automate leave request approvals.
Explanation: This flow triggers on form submission, sends approval requests to managers, and updates the status in Dataverse based on the manager’s response.
Dataverse Schema:

Use Case: Store leave request data.
Explanation: The schema includes fields for employee details, leave dates, and approval status.
Power Apps:

Use Case: Submit and track leave requests.
Explanation: Power Apps provides an interface for employees to submit leave requests and track their status.
Power Pages:

Use Case: Manager portal for approvals.
Explanation: A portal for managers to view and approve leave requests.
JavaScript:

Use Case: Validate leave dates.
Explanation: A script validates that the end date is not before the start date when submitting a leave request.
Python:

Use Case: Submit leave requests.
Explanation: A Python script interacts with the Dataverse API to submit leave requests.
Power BI:

Use Case: Track leave data.
Explanation: Dashboards track leave requests, approval times, and leave balances.
