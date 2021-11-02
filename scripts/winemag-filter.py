import pandas as pd

df = pd.read_csv(r'datasets\winemag-1-800.csv')
filtered = df["country"] == "Portugal"
df = df[filtered]

df1 = pd.read_csv(r'datasets\winemag-1601-2400.csv')
filtered = df1["country"] == "Portugal"
df1 = df1[filtered]

df2 = pd.read_csv(r'datasets\winemag-2401-3200.csv')
df2 = pd.read_csv(r'datasets\winemag-1601-2400.csv')
filtered = df2["country"] == "Portugal"
df2 = df2[filtered]


df3 = pd.read_csv(r'datasets\winemag-3201-4000.csv')
df3 = pd.read_csv(r'datasets\winemag-1601-2400.csv')
filtered = df3["country"] == "Portugal"
df3 = df3[filtered]

df4 = pd.read_csv(r'datasets\winemag-4001-4800.csv')
df4 = pd.read_csv(r'datasets\winemag-1601-2400.csv')
filtered = df4["country"] == "Portugal"
df4 = df4[filtered]

df5 = pd.read_csv(r'datasets\winemag-4801-5600.csv')
df5 = pd.read_csv(r'datasets\winemag-1601-2400.csv')
filtered = df5["country"] == "Portugal"
df5 = df5[filtered]

df6 = pd.read_csv(r'datasets\winemag-5601-6400.csv')
df6 = pd.read_csv(r'datasets\winemag-1601-2400.csv')
filtered = df6["country"] == "Portugal"
df6 = df6[filtered]

df7 = pd.read_csv(r'datasets\winemag-6401-7200.csv')
df7 = pd.read_csv(r'datasets\winemag-1601-2400.csv')
filtered = df7["country"] == "Portugal"
df7 = df7[filtered]

df8 = pd.read_csv(r'datasets\winemag-7201-8000.csv')
df8 = pd.read_csv(r'datasets\winemag-1601-2400.csv')
filtered = df8["country"] == "Portugal"
df8 = df8[filtered]

df9 = pd.read_csv(r'datasets\winemag-8001-8800.csv')
df9 = pd.read_csv(r'datasets\winemag-1601-2400.csv')
filtered = df9["country"] == "Portugal"
df9 = df9[filtered]

df10 = pd.read_csv(r'datasets\winemag-8801-9600.csv')
df10 = pd.read_csv(r'datasets\winemag-1601-2400.csv')
filtered = df10["country"] == "Portugal"
df10 = df10[filtered]

df11 = pd.read_csv(r'datasets\winemag-9601-10400.csv')
df11 = pd.read_csv(r'datasets\winemag-1601-2400.csv')
filtered = df11["country"] == "Portugal"
df11 = df11[filtered]

df12 = pd.read_csv(r'datasets\winemag-10401-11200.csv')
df12 = pd.read_csv(r'datasets\winemag-1601-2400.csv')
filtered = df12["country"] == "Portugal"
df12 = df12[filtered]

df13 = pd.read_csv(r'datasets\winemag-11201-12000.csv')
df13 = pd.read_csv(r'datasets\winemag-1601-2400.csv')
filtered = df13["country"] == "Portugal"
df13 = df13[filtered]

df14 = pd.read_csv(r'datasets\winemag-12001-12800.csv')
df14 = pd.read_csv(r'datasets\winemag-1601-2400.csv')
filtered = df14["country"] == "Portugal"
df14 = df14[filtered]

fin = [df, df1, df2, df3, df4, df5, df6, df7,
       df8, df9, df10, df11, df12, df13, df14]
result = pd.concat(fin)
result.to_csv(r'datasets/winemag-filtered.csv')
