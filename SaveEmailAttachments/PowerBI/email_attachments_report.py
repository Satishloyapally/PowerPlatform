import pandas as pd
import matplotlib.pyplot as plt

# Sample data - replace with your actual data source
data = {
    'Date': ['2023-05-01', '2023-05-02', '2023-05-03', '2023-05-04'],
    'EmailSubject': ['Subject 1', 'Subject 2', 'Subject 3', 'Subject 4'],
    'Sender': ['sender1@example.com', 'sender2@example.com', 'sender3@example.com', 'sender4@example.com'],
    'AttachmentName': ['file1.pdf', 'file2.pdf', 'file3.pdf', 'file4.pdf'],
    'FileURL': ['url1', 'url2', 'url3', 'url4']
}

# Create DataFrame
df = pd.DataFrame(data)

# Save DataFrame to CSV (or directly connect to your data source)
df.to_csv('email_attachments.csv', index=False)

# Load data into Power BI
df = pd.read_csv('email_attachments.csv')

# Plotting example: Frequency of email attachments per day
df['Date'] = pd.to_datetime(df['Date'])
attachments_per_day = df.groupby(df['Date'].dt.date).size()

# Create a bar plot
plt.figure(figsize=(10, 6))
attachments_per_day.plot(kind='bar', color='skyblue')
plt.title('Frequency of Email Attachments Saved per Day')
plt.xlabel('Date')
plt.ylabel('Number of Attachments')
plt.xticks(rotation=45)
plt.tight_layout()

# Save plot as an image file
plt.savefig('attachments_per_day.png')

# Show plot (for local testing)
plt.show()

#Explanation:

#Data Loading: The script reads email attachment data from a CSV file.
#Data Analysis: It counts the number of attachments sent by each sender.
#Visualization: A bar chart displays the frequency of attachments per sender.
