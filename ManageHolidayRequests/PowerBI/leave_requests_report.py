iimport pandas as pd
import matplotlib.pyplot as plt

# Sample data - replace with your actual data source
data = {
    'Employee': ['John Doe', 'Jane Smith', 'Alice Johnson', 'Bob Brown'],
    'StartDate': ['2023-06-01', '2023-06-05', '2023-06-10', '2023-06-15'],
    'EndDate': ['2023-06-10', '2023-06-12', '2023-06-20', '2023-06-25'],
    'Status': ['Approved', 'Pending', 'Approved', 'Rejected']
}

# Create DataFrame
df = pd.DataFrame(data)

# Save DataFrame to CSV (or directly connect to your data source)
df.to_csv('leave_requests.csv', index=False)

# Load data into Power BI
df = pd.read_csv('leave_requests.csv')

# Plotting example: Number of leave requests by status
status_counts = df['Status'].value_counts()

# Create a bar plot
plt.figure(figsize=(10, 6))
status_counts.plot(kind='bar', color='skyblue')
plt.title('Number of Leave Requests by Status')
plt.xlabel('Status')
plt.ylabel('Number of Requests')
plt.xticks(rotation=0)
plt.tight_layout()

# Save plot as an image file
plt.savefig('leave_requests_status.png')

# Show plot (for local testing)
plt.show()

