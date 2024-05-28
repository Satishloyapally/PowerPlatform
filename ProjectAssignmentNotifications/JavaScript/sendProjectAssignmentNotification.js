function sendProjectAssignmentNotification(project) {
    let notificationMessage = `You have been assigned a new project: ${project.name}`;
    alert(notificationMessage);
}

document.getElementById("assignProjectButton").addEventListener("click", sendProjectAssignmentNotification);

