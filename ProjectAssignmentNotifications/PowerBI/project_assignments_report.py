import pandas as pd
import matplotlib.pyplot as plt

# Sample data - replace with your actual data source
data = {
    'EmployeeName': ['John Doe', 'Jane Smith', 'Alice Johnson', 'Bob Brown'],
    'ProjectName': ['Project A', 'Project B', 'Project C', 'Project D'],
    'AssignmentDate': ['2023-06-01', '2023-06-05', '2023-06-10', '2023-06-15']
}

# Create DataFrame
df = pd.DataFrame(data)

# Save DataFrame to CSV (or directly connect to your data source)
df.to_csv('project_assignments.csv', index=False)

# Load data into Power BI
df = pd.read_csv('project_assignments.csv')

# Plotting example: Number of project assignments by employee
assignments_per_employee = df['EmployeeName'].value_counts()

# Create a bar plot
plt.figure(figsize=(10, 6))
assignments_per_employee.plot(kind='bar', color='skyblue')
plt.title('Number of Project Assignments by Employee')
plt.xlabel('Employee')
plt.ylabel('Number of Assignments')
plt.xticks(rotation=45)
plt.tight_layout()

# Save plot as an image file
plt.savefig('project_assignments_per_employee.png')

# Show plot (for local testing)
plt.show()

