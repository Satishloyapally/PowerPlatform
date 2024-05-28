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

