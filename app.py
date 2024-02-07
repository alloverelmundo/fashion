#Step 1 - cleaning data
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

#Step 2 - Price Analysis 

#Calculate average selling price and original price across different categories
price_analysis = df.groupby('category').agg(
    avg_selling_price=('selling_price', 'mean'),
    avg_original_price=('original_price', 'mean')
).reset_index()

# Print the price analysis
print("Price Analysis:")
print(price_analysis)

#Price Analysis Findings

#INSERT HERE

#Step 3 - Availability Analysis

# Calculate the percentage of products in stock versus out-of-stock
availability_analysis = df['availability'].value_counts(normalize=True) * 100

# Print the availability analysis
print("Availability Analysis:")
print(availability_analysis)

#Step 4 - Rating and Reviews Analysis
# Calculate the average rating and total number of reviews for products in each category
rating_reviews_analysis = df.groupby('category').agg(
    avg_rating=('average_rating', 'mean'),
    total_reviews=('reviews_count', 'sum')
).reset_index()

# Print the rating and reviews analysis
print("\nRating and Reviews Analysis:")
print(rating_reviews_analysis)

#Step 5 - Categorical Analysis
# Analyze the distribution of products across different categories, colors, or sources
categorical_analysis = df.groupby(['category', 'color', 'source']).size().reset_index(name='count')

# Print the categorical analysis
print("\nCategorical Analysis:")
print(categorical_analysis)

#Step 6 - Brand Analysis
# Investigate the market share of different brands based on the number of products or total sales
brand_analysis = df['brand'].value_counts(normalize=True) * 100

# Print the brand analysis
print("Brand Analysis:")
print(brand_analysis)

# Calculate the average selling price and rating among different brands
brand_price_rating_analysis = df.groupby('brand').agg(
    avg_selling_price=('selling_price', 'mean'),
    avg_rating=('average_rating', 'mean')
).reset_index()

# Print the brand price and rating analysis
print("\nBrand Price and Rating Analysis:")
print(brand_price_rating_analysis)
