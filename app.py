#insert code here

#CLEAING DATA
import pandas as pd

# Load the dataset
csv_file_path = '/Users/vk/Desktop/vscodepractice/fashionproject/adidas/adidas_usa.csv'

# Read CSV into a pandas DataFrame
df = pd.read_csv(csv_file_path)

# Print the initial dataset
print("Initial Dataset:")
print(df)

# Cleaning steps
# Handling missing values
df.fillna({'selling_price': 0, 'original_price': 0, 'average_rating': 0, 'reviews_count': 0}, inplace=True)

# Removing duplicates
df.drop_duplicates(inplace=True)

# Correcting data types
df['selling_price'] = df['selling_price'].astype(float)
df['original_price'] = df['original_price'].astype(float)
df['average_rating'] = df['average_rating'].astype(float)
df['reviews_count'] = df['reviews_count'].astype(int)

# Standardizing formats (e.g., lowercase)
df['name'] = df['name'].str.lower()
df['color'] = df['color'].str.lower()
df['category'] = df['category'].str.lower()
df['source'] = df['source'].str.lower()
df['brand'] = df['brand'].str.lower()
df['country'] = df['country'].str.upper()
df['language'] = df['language'].str.lower()

# Print the cleaned dataset
print("\nCleaned Dataset:")
print(df)
