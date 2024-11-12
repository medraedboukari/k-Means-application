import pandas as pd

# Create a sample dataset 
data = {
    'Industry': ['Technology', 'Healthcare', 'Finance', 'Technology', 'Arts', 'Finance', 'Healthcare', 'Arts', 'Technology', 'Finance'],
    'Experience_Years': [5, 10, 15, 2, 20, 12, 7, 8, 3, 9],
    'Interest': ['AI', 'Public Health', 'Investment', 'Machine Learning', 'Digital Art', 'Stock Analysis', 'Biotech', 'Painting', 'AI', 'Banking']
}

# Convert the dataset to a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
csv_file_path = 'networking_event_attendees.csv'
df.to_csv(csv_file_path, index=False)


