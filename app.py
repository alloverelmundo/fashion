#The cleaned version of analyzing Adidas data. 
#About this dataset
#This dataset contains information on over 1500+ Adidas fashion products. 
#The data includes fields such as name, selling price, original price, currency, availability, color, category, source website, breadcrumbs, description, brand, images, country, language, average rating and reviews count. 
#This data was collected from a variety of sources and compiled into one dataset for research purposes.
#This Adidas fashion dataset provides rich product information for over 9300+ products. 
#It contains detailed information on product selling price, original price in multiple currencies ( USD / EUR / GBP ), product availability ( in stock / out of stock ), color , Category ( such as Apparel / Footwear ), source website , breadcrumbs , product description , brand name , link to product images , Country of origin and language . 
#The average rating and reviews count are also included in the dataset so that researchers can study the correlation between them.

#Research Ideas
#This dataset can be used to determine which colors are most popular among different age groups or genders.
#This dataset can be used to identify the most popular products among different countries or regions.
#This dataset can be used to analyze the correlation between product reviews and ratings to determine which factors are most important to customers.

#Column name:	Description
#url:	The URL of the product page on the source website. (String)
#name:	The name of the product. (String)
#sku:	The SKU or unique identifier for the product. (String)
#selling_price:	The selling price of the product in USD or Euros. (Float)
#original_price:	The original price of the product in USD or Euros. (Float)
#currency:	The currency type for the selling price and original price. (String)
#availability:	The availability of the product. (String)
#color:	The color of the product. (String)
#category:	The category of the product. (String)
#source_website:	The source website from where the data was collected. (String)
#breadcrumbs:	The breadcrumbs or path to the product page on the source website. (String)
#description:	A brief description of the product provided by Adidas. (String)
#brand:	The brand of the product. (String)
#images:	Multiple product images provided by Adidas. (String)
#country:	The country of origin/destination for the product. (String)
#language:	The language in which the product page was displayed on the source website. (String)
#average_rating:	The average customer rating out of 5 stars. (Float)
#reviews_count:	The number of customer reviews for the product. (Integer)
#crawled_at:	The date and time when the data was collected. (String)

#Step 1- data cleaning, importing packages, etc. 
#importing all necessary packages for analysis and cleaning
import numpy as np
import pandas as pd
import requests
import matplotlib.pyplot as plt
import scipy as sp 
from matplotlib import pyplot as plt
import scipy.stats as stats
from sklearn.preprocessing import MinMaxScaler
from scipy import stats

#getting data from csv file and cleaning
df_adidas = pd.read_csv('adidas_usa.csv')

#remove any rows with missing data
df_adidas = df_adidas.dropna(axis=0, how='any')

#changing the index numbers because they were off by 15
df_adidas['index'] -= 15

#calculating the differences between sale price and original price and putting in new column
#first converting to float value
df_adidas['original_price'] = df_adidas['original_price'].str.replace('$','').astype(float)
df_adidas['selling_price'] = pd.to_numeric(df_adidas['selling_price'])
df_adidas['price_difference'] = df_adidas['original_price'] - df_adidas['selling_price']

#dropping any duplicates
df_adidas.drop_duplicates(inplace=True)

#converting other values 
df_adidas['average_rating'] = df_adidas['average_rating'].astype(float)
df_adidas['reviews_count'] = df_adidas['reviews_count'].astype(int)

#dropping irrelevant columns
df_adidas= df_adidas.drop(columns=['currency', 'brand', 'country', 'language', 'crawled_at'])

#Step 2 - Price Analysis 

#Calculate the average selling price and original price across different categories
price_analysis = df_adidas.groupby('category').agg(
    avg_selling_price=('selling_price', 'mean'),
    avg_original_price=('original_price', 'mean')
).reset_index()

# Print the price analysis
print("Price Analysis:")
print(price_analysis)

#Price Analysis Findings
#The average selling price for Accessories is $29.38 and the average original price is $35.43.
#The average selling price for Clothing is $38.73 and the average original price is $49.33.
#The average selling price for Accessories is $68.90 and the average original price is $90.58.

#Step 3 - Availability Analysis

# Calculate the percentage of products in stock versus out-of-stock
availability_analysis = df_adidas['availability'].value_counts(normalize=True) * 100

# Print the availability analysis
print("Availability Analysis:")
print(availability_analysis)

#Availability Analysis Findings
#Generally, the products were available 99.64% of the time.

#Step 4 - Rating and Reviews Analysis
# Calculate the average rating and total number of reviews for products in each category
rating_reviews_analysis = df_adidas.groupby('category').agg(
    avg_rating=('average_rating', 'mean'),
    total_reviews=('reviews_count', 'sum')
).reset_index()

# Print the rating and reviews analysis
print("\nRating and Reviews Analysis:")
print(rating_reviews_analysis)

#Ratings and Reviews Analysis
#Accessories have an average rating of 4.83, and total reviews of 3,997.
#Clothing has an average rating of 4.64, and total reviews of 22,265.
#Shoes have an average rating of 4.54, and total reviews of 333,477.

#Step 5 - Categorical Analysis
# Analyze the distribution of products across different categories, colors, or sources
categorical_analysis = df_adidas.groupby(['category', 'color', 'source']).size().reset_index(name='count')

# Print the categorical analysis
print("\nCategorical Analysis:")
print(categorical_analysis)

#Step 6 - Text Analysis
# Analyze product descriptions to identify common keywords or phrases
# Counting the occurrence of each word in the descriptions
word_counts = df_adidas['description'].str.split(expand=True).stack().value_counts()

# Print the top 10 most common words in descriptions
print("Top 10 most common words in descriptions:")
print(word_counts.head(10))


