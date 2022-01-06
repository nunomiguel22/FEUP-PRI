import pandas as pd
import matplotlib.pyplot as plt

INFO_FILE = 'datasets/vivino-info.csv'
REVIEW_FILE = 'datasets/vivino_reviews_2.csv'

df_info = pd.read_csv(INFO_FILE)
df_reviews = pd.read_csv(REVIEW_FILE)

#df_reviews = df_reviews.drop(col3umns=['rating', 'user'], axis=1)

df_reviews = df_reviews.groupby(['id'])['note'].apply('}'.join).reset_index()

df_final = pd.merge(df_info, df_reviews, how='left')

# print(df_final)

df_final.to_csv('datasets/vivino_reviews_final.csv', index=True)

# %7D
