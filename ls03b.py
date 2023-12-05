import pandas as pd

df = pd.read_csv("countries.csv")


df["lat1"] = df["latitude"] * 2
df["lat2"] = df["latitude"] / df["longitude"]

print(df.head())


df2 = pd.read_csv("persons.csv")

df2["age_total_days"] = df2["age_days"] + df2["age_years"] * 365

print(df2.head())
