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

#Explanation:

#Purpose: Send document approval notifications to Microsoft Teams.
#Function: send_approval_notification(document)
#Steps:
#Define the Microsoft Teams API endpoint for sending messages.
#Set up headers with authorization and content type.
#Prepare the notification message data.
#Send a POST request with the notification data.
#Check the response status to confirm the success or failure of the operation.
