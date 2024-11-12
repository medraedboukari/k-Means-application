import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder

# Sample dataset representing attendees
df = pd.read_csv('networking_event_attendees.csv')

# Convert the dataset to a DataFrame
df = pd.DataFrame(df)

# Initialize LabelEncoder
label_encoder = LabelEncoder()

# Encode categorical variables  into numerical values
df['Industry'] = label_encoder.fit_transform(df['Industry'])
df['Interest'] = label_encoder.fit_transform(df['Interest'])

# Prepare the feature set 
X = df[['Industry', 'Experience_Years', 'Interest']]

# Standardize the data 
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply K-means clustering 
kmeans = KMeans(n_clusters=3, random_state=0)
df['Cluster'] = kmeans.fit_predict(X_scaled)


print("Clustered Attendees:")
print(df)

# Visualize the clusters 
fig, ax = plt.subplots(figsize=(10, 6))

# Plotting Experience_Years vs. Industry
scatter = ax.scatter(df['Experience_Years'], df['Industry'], c=df['Cluster'], s=100, cmap='viridis')
legend = ax.legend(*scatter.legend_elements(), title='Clusters')
ax.add_artist(legend)

# Add cluster centers 
centers = kmeans.cluster_centers_

# Plot the cluster 
ax.scatter(centers[:, 1], centers[:, 0], c='red', s=200, marker='X', label='Centroids')

ax.set_title('Clusters of Attendees by Industry, Experience, and Interest')
ax.set_xlabel('Experience Years')
ax.set_ylabel('Industry (Encoded)')
ax.grid(True)


plt.show()
