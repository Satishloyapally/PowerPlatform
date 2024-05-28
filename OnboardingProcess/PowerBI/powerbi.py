import pandas as pd
import matplotlib.pyplot as plt

# Sample data - replace with your actual data source
data = {
    'Employee': ['John Doe', 'Jane Smith', 'Alice Johnson', 'Bob Brown'],
    'Task': ['Complete paperwork', 'Attend orientation', 'Setup workstation', 'Meet team'],
    'CompletionStatus': ['Completed', 'Pending', 'Completed', 'Pending'],
    'DueDate': ['2023-05-01', '2023-05-02', '2023-05-03', '2023-05-04']
}

# Create DataFrame
df = pd.DataFrame(data)

# Save DataFrame to CSV (or directly connect to your data source)
df.to_csv('onboarding_tasks.csv', index=False)

# Load data into Power BI
df = pd.read_csv('onboarding_tasks.csv')

# Plotting example: Onboarding tasks completion status
completion_counts = df['CompletionStatus'].value_counts()

# Create a pie chart
plt.figure

