import requests

def save_attachment_to_sharepoint(email):
    url = f"https://your-sharepoint-site/_api/web/GetFolderByServerRelativeUrl('/Shared Documents/Attachments')/Files/add(url='{email['attachment']['name']}',overwrite=true)"
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Accept': 'application/json;odata=verbose',
        'Content-Type': 'application/json'
    }
    response = requests.post(url, headers=headers, data=email['attachment']['content'])
    if response.status_code == 200:
        print("Attachment saved successfully")
    else:
        print("Error saving attachment: ", response.status_code)

