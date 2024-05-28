import pandas as pd
import matplotlib.pyplot as plt

# Sample data - replace with your actual data source
data = {
    'EmployeeName': ['John Doe', 'Jane Smith', 'Alice Johnson', 'Bob Brown'],
    'StartDate': ['2023-06-01', '2023-06-05', '2023-06-10', '2023-06-15'],
    'OnboardingStatus': ['Completed', 'Pending', 'Completed', 'In Progress']
}

# Create DataFrame
df = pd.DataFrame(data)

# Save DataFrame to CSV (or directly connect to your data source)
df.to_csv('onboarding.csv', index=False)

# Load data into Power BI
df = pd.read_csv('onboarding.csv')

# Plotting example: Onboarding status of employees
status_counts = df['OnboardingStatus'].value_counts()

# Create a bar plot
plt.figure(figsize=(10, 6))
status_counts.plot(kind='bar', color='skyblue')
plt.title('Onboarding Status of Employees')
plt.xlabel('Status')
plt.ylabel('Number of Employees')
plt.xticks(rotation=0)
plt.tight_layout()

# Save plot as an image file
plt.savefig('onboarding_status.png')

# Show plot (for local testing)
plt.show()

#Explanation:

#Data Loading: The script reads onboarding data from a CSV file.
#Data Analysis: It counts the number of employees in each onboarding status category.
#Visualization: A bar chart displays the number of employees by their onboarding status.
