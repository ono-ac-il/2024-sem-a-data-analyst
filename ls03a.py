import pandas as pd

df = pd.read_csv("countries.csv")

print(df.sort_values(by="latitude", ascending=False).head())
