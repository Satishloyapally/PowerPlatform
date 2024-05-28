function validateInvoiceData(invoice) {
    if (invoice.amount <= 0) {
        alert("Invoice amount must be greater than zero.");
        return false;
    }
    return true;
}

document.getElementById("uploadInvoiceButton").addEventListener("click", validateInvoiceData);

//Explanation:

//Purpose: Validate invoice data before processing.
//Function: validateInvoiceData(invoice)
//Steps:
//Check if the invoice amount is greater than zero.
//Show an alert if the validation fails.
//Add an event listener to the upload invoice button to trigger the validation function.
