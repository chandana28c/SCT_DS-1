import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load your dataset (replace 'your_dataset.csv' with your actual file)
# Make sure it contains columns: 'Age' and 'Gender'
data = pd.read_csv('sample_population_data.csv')

# Create and save Age Distribution Histogram
plt.figure(figsize=(8, 5))
sns.histplot(data['Age'], bins=10, kde=True, color='skyblue')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig('age_distribution.png')
plt.close()

# Create and save Gender Distribution Bar Chart
plt.figure(figsize=(6, 5))
sns.countplot(x='Gender', data=data, palette='pastel')
plt.title('Gender Distribution')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('gender_distribution.png')
plt.close()

print("Charts created and saved successfully.")
