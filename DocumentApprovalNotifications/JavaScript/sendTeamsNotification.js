function sendTeamsNotification(document) {
    let teamsMessage = `Document ${document.name} has been approved.`;
    microsoftTeams.executeDeepLink(teamsMessage);
}

document.getElementById("approveButton").addEventListener("click", sendTeamsNotification);

