import requests

def extract_data_from_invoice(invoice):
    url = "https://your-ai-builder-site/api/extract"
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    data = {
        'invoice': invoice
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        extracted_data = response.json()
        store_invoice_data(extracted_data)
    else:
        print("Error extracting data: ", response.status_code)

def store_invoice_data(data):
    url = "https://your-dataverse-site/api/data/v9.0/Invoices"
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 201:
        print("Invoice data stored successfully")
    else:
        print("Error storing invoice data: ", response.status_code)

#Explanation:

#Purpose: Extract and store invoice data using AI Builder and Dataverse.
#Functions: extract_data_from_invoice(invoice) and store_invoice_data(data)
#Steps:
#Extract Data:
#Define the AI Builder API endpoint for extracting data from invoices.
#Set up headers with authorization and content type.
#Prepare the invoice data.
#Send a POST request with the invoice data.
#Check the response status and extract the data.
#Store Data:
#Define the Dataverse API endpoint for storing invoice data.
#Set up headers with authorization and content type.
#Send a POST request with the extracted invoice data.
#Check the response status to confirm the success or failure of the operation.
