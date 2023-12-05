import pandas as pd

df = pd.read_csv("countries.csv")
df2 = pd.read_csv("persons.csv")

# TODO:
df = df.rename(columns={"name": "country_name"})
print(df.head())
df3 = pd.concat([df, df2])


print(df3.head())
print(df.shape)
print(df2.shape)
print(df3.shape)

# print(df3.describe())

# print(df3.agg({"country_name": ["count"], "latitude": ["count", "mean", "min", "max"]}))

# print(df3["name"].notna())

print(df3["name"].fillna("not"))
# print(df3["name"].dropna())
