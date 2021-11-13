"""
    Module for displaying statistics from vivino.com for wine information
"""

import pandas as pd
import matplotlib.pyplot as plt

INFO_FILE = 'datasets/vivino-info.csv'
REVIEW_FILE = 'datasets/vivino-reviews.csv'

df = pd.read_csv(INFO_FILE)

print('DATASET ANALYSIS', end='\n\n')

print('NULL VALUE COUNT')
print(df.isnull().sum(), end='\n\n')

print('RATING AND PRICE')
print(df[['rating', 'price']].describe(), end='\n\n')

print('REGION COUNT')
print(df['region'].value_counts(), end='\n\n')

print('WINE TYPE')
print(df['type'].value_counts(), end='\n\n')

print('YEAR DISTRIBUTION')
print(df['year'].value_counts(), end='\n\n')

year_rating_dist = df[['year', 'rating']].groupby('year').mean()
yr_plot = year_rating_dist.plot()
yr_plot.set_title('Rating average for each year')

plt.show()
