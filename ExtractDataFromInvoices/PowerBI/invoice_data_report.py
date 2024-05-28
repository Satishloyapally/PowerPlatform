import pandas as pd
import matplotlib.pyplot as plt

# Sample data - replace with your actual data source
data = {
    'InvoiceNumber': ['INV001', 'INV002', 'INV003', 'INV004'],
    'Amount': [1500, 2500, 1750, 2000],
    'InvoiceDate': ['2023-05-01', '2023-05-02', '2023-05-03', '2023-05-04'],
    'SupplierName': ['Supplier A', 'Supplier B', 'Supplier C', 'Supplier D']
}

# Create DataFrame
df = pd.DataFrame(data)

# Save DataFrame to CSV (or directly connect to your data source)
df.to_csv('invoices.csv', index=False)

# Load data into Power BI
df = pd.read_csv('invoices.csv')

# Plotting example: Total invoice amount per supplier
total_amount_per_supplier = df.groupby('SupplierName')['Amount'].sum()

# Create a bar plot
plt.figure(figsize=(10, 6))
total_amount_per_supplier.plot(kind='bar', color='skyblue')
plt.title('Total Invoice Amount per Supplier')
plt.xlabel('Supplier')
plt.ylabel('Total Amount')
plt.xticks(rotation=45)
plt.tight_layout()

# Save plot as an image file
plt.savefig('total_amount_per_supplier.png')

# Show plot (for local testing)
plt.show()

