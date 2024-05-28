import requests

def send_project_assignment_notification(employee, project):
    url = "https://your-email-service/api/send"
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    data = {
        'to': employee['email'],
        'subject': 'New Project Assignment',
        'body': f'You have been assigned a new project: {project["name"]}'
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        print("Notification sent successfully")
    else:
        print("Error sending notification: ", response.status_code)

