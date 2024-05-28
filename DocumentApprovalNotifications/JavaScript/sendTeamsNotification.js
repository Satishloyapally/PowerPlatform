function sendTeamsNotification(document) {
    let teamsMessage = `Document ${document.name} has been approved.`;
    microsoftTeams.executeDeepLink(teamsMessage);
}

document.getElementById("approveButton").addEventListener("click", sendTeamsNotification);

//Explanation:

//Purpose: Send notifications to Microsoft Teams when a document is approved.
//Function: sendTeamsNotification(document)
//Steps:
//Create a message with the document name.
//Use Microsoft Teams API to send the message.
//Add an event listener to the approve button to trigger the notification function.
