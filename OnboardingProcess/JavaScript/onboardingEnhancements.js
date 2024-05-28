function sendOnboardingMaterials(employee) {
    let onboardingMessage = `Welcome ${employee.name}! Here are your onboarding materials.`;
    alert(onboardingMessage);
}

document.getElementById("sendOnboardingButton").addEventListener("click", sendOnboardingMaterials);

//Explanation:

//Purpose: Send onboarding materials to new employees.
//Function: sendOnboardingMaterials(employee)
//Steps:
//Create an onboarding message with the employee's name.
//Show an alert with the onboarding message.
//Add an event listener to the onboarding button to trigger the function.
