"""
Remove year from the name field in BlogOsVinhos.csv
"""

import pandas as pd

df = pd.read_csv('datasets/BlogOsVinhos.csv')

name_col = df['Name']


for i in range(len(name_col)):
    name_col[i] = name_col[i].rsplit(' ', 1)[0] #Cut off all characters after the last space


df["name"] = name_col

df.to_csv('datasets/BlogOsVinhos_no_year.csv')
