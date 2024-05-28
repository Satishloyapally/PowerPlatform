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

