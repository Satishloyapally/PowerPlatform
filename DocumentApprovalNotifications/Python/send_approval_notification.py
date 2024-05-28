import requests

def send_approval_notification(document):
    url = "https://your-teams-site/api/messages"
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    data = {
        'message': f'Document {document["name"]} has been approved.'
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 201:
        print("Notification sent successfully")
    else:
        print("Error sending notification: ", response.status_code)

