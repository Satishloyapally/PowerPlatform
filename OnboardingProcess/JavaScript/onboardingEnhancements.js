function sendOnboardingMaterials(employee) {
    let onboardingMessage = `Welcome ${employee.name}! Here are your onboarding materials.`;
    alert(onboardingMessage);
}

document.getElementById("sendOnboardingButton").addEventListener("click", sendOnboardingMaterials);

