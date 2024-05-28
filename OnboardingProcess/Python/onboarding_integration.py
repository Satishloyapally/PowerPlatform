import requests

def send_onboarding_materials(employee):
    url = "https://your-email-service/api/send"
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    data = {
        'to': employee['email'],
        'subject': 'Welcome to the Team!',
        'body': f'Hello {employee["name"]}, welcome to the team! Here are your onboarding materials.'
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        print("Onboarding materials sent successfully")
    else:
        print("Error sending onboarding materials: ", response.status_code)

def schedule_onboarding_meeting(employee):
    url = "https://your-outlook-service/api/create_event"
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    data = {
        'subject': 'Onboarding Meeting',
        'start': employee['start_time'],
        'end': employee['end_time'],
        'attendees': [employee['email']]
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 201:
        print("Onboarding meeting scheduled successfully")
    else:
        print("Error scheduling onboarding meeting: ", response.status_code)

#Explanation:

#Purpose: Send onboarding materials and schedule meetings.
#Functions: send_onboarding_materials(employee) and schedule_onboarding_meeting(employee)
#Steps:
#Send Onboarding Materials:
#Define the email service API endpoint for sending onboarding materials.
#Set up headers with authorization and content type.
#Prepare the onboarding email data.
#Send a POST request with the onboarding email data.
#Check the response status to confirm the success or failure of the operation.
#Schedule Onboarding Meeting:
#Define the Outlook API endpoint for scheduling events.
#Set up headers with authorization and content type.
#Prepare the meeting data.
#Send a POST request with the meeting data.
#Check the response status to confirm the success or failure of the operation.
