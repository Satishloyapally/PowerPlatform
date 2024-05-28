function sendProjectAssignmentNotification(project) {
    let notificationMessage = `You have been assigned a new project: ${project.name}`;
    alert(notificationMessage);
}

document.getElementById("assignProjectButton").addEventListener("click", sendProjectAssignmentNotification);

//Explanation:

//Purpose: Notify employees about new project assignments in Power Apps.
//Function: sendProjectAssignmentNotification(project)
//Steps:
//Create a notification message with the project name.
//Show an alert with the notification message.
//Add an event listener to the project assignment button to trigger the notification function.
