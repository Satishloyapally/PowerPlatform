import pandas as pd
import matplotlib.pyplot as plt

# Sample data - replace with your actual data source
data = {
    'DocumentName': ['Doc1', 'Doc2', 'Doc3', 'Doc4'],
    'ApprovalStatus': ['Approved', 'Pending', 'Approved', 'Rejected'],
    'ApprovalDate': ['2023-05-01', '2023-05-02', '2023-05-03', '2023-05-04'],
    'Approver': ['Alice', 'Bob', 'Charlie', 'David']
}

# Create DataFrame
df = pd.DataFrame(data)

# Save DataFrame to CSV (or directly connect to your data source)
df.to_csv('document_approvals.csv', index=False)

# Load data into Power BI
df = pd.read_csv('document_approvals.csv')

# Plotting example: Number of document approvals by status
status_counts = df['ApprovalStatus'].value_counts()

# Create a bar plot
plt.figure(figsize=(10, 6))
status_counts.plot(kind='bar', color='skyblue')
plt.title('Number of Document Approvals by Status')
plt.xlabel('Status')
plt.ylabel('Number of Approvals')
plt.xticks(rotation=0)
plt.tight_layout()

# Save plot as an image file
plt.savefig('document_approvals_status.png')

# Show plot (for local testing)
plt.show()

