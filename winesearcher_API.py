"""
Remove year from the name field in BlogOsVinhos.csv
"""

import pandas as pd

df = pd.read_csv('datasets/winemag-final.csv')


df['BJudge'] = ""
df['BJudgeRating'] = ""
df['BJudgeNotes'] = ""
df['BLink'] = ""

df.to_csv('datasets/wm.csv')
