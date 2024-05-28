function validateInvoiceData(invoice) {
    if (invoice.amount <= 0) {
        alert("Invoice amount must be greater than zero.");
        return false;
    }
    return true;
}

document.getElementById("uploadInvoiceButton").addEventListener("click", validateInvoiceData);

