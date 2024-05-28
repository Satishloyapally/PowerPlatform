import requests

def submit_leave_request(employee, start_date, end_date):
    url = "https://your-dataverse-site/api/data/v9.0/LeaveRequests"
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    data = {
        'employee': employee,
        'start_date': start_date,
        'end_date': end_date,
        'status': 'Pending'
    }
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 201:
        print("Leave request submitted successfully")
    else:
        print("Error submitting leave request: ", response.status_code)

#Explanation:

#Purpose: Submit leave requests to Dataverse.
#Function: submit_leave_request(employee, start_date, end_date)
#Steps:
#Define the Dataverse API endpoint for adding new leave requests.
#Set up headers with authorization and content type.
#Prepare the leave request data.
#Send a POST request with the leave request data.
#Check the response status to confirm the success or failure of the operation.
