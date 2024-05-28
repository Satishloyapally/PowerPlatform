# Automatically Save Email Attachments
SaveEmailAttachments
├── PowerAutomate
│   └── save_email_attachments_flow.json
├── Dataverse
│   └── schema.json
├── PowerApps
│   └── [PowerApps Project Files]
├── PowerPages
│   └── index.html
├── JavaScript
│   └── filterAttachments.js
├── Python
│   └── save_attachment.py
├── PowerBI
│   └── email_attachments_report.py
└── README.md

# Save Email Attachments

This project automates the process of saving email attachments to SharePoint using Microsoft Power Platform.

## Project Structure
- **PowerAutomate**: Contains the flow definition JSON file.
- **Dataverse**: Contains the schema for the Dataverse table.
- **PowerApps**: Contains Power Apps project files.
- **PowerPages**: Contains HTML files for Power Pages.
- **JavaScript**: Contains JavaScript code to enhance Power Apps.
- **Python**: Contains Python scripts for integration.
- **PowerBI**: Contains Python scripts to generate Power BI reports.

- 1. Automatically Save Email Attachments
Power Automate Flow:

Use Case: Automatically saves email attachments to SharePoint.
Explanation: This flow triggers when a new email arrives, checks for attachments, and saves them to a specified SharePoint folder. It uses the "When a new email arrives (V3)" trigger and "Create file" action.
Dataverse Schema:

Use Case: Store metadata about attachments.
Explanation: The Dataverse schema includes fields like email subject, sender, attachment name, and file URL. This metadata is stored for tracking and reporting purposes.
Power Apps:

Use Case: View and manage saved attachments.
Explanation: Power Apps connects to the Dataverse table and provides a user interface to display and manage attachments.
Power Pages:

Use Case: Provide web access to attachments.
Explanation: A web page developed using Power Pages allows users to access and download attachments.
JavaScript:

Use Case: Enhance Power Apps functionality.
Explanation: A script filters attachments in the Power Apps gallery based on user input.
Python:

Use Case: Integration with SharePoint.
Explanation: A Python script uses the SharePoint API to save attachments programmatically.
Power BI:

Use Case: Analyze email attachment data.
Explanation: Power BI dashboards provide insights into the frequency and volume of saved attachments.
