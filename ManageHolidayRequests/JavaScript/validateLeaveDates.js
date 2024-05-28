function validateLeaveDates() {
    let startDate = new Date(document.getElementById("startDateInput").value);
    let endDate = new Date(document.getElementById("endDateInput").value);
    if (endDate < startDate) {
        alert("End date cannot be before start date.");
        return false;
    }
    return true;
}

document.getElementById("submitLeaveRequest").addEventListener("click", validateLeaveDates);

//Explanation:

//Purpose: Validate leave request dates in Power Apps.
//Function: validateLeaveDates()
//Steps:
//Get the start and end dates from the input fields.
//Convert the input values to Date objects.
//Check if the end date is before the start date.
//Show an alert if the validation fails.
//Add an event listener to the submit button to trigger the validation function.
