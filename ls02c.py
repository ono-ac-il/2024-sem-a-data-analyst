import pandas as pd

# Statistics
df = pd.read_csv("countries.csv")

# Average
# print(df["latitude"].mean())

# median
# print(df["latitude"].median())

cols = ["latitude", "longitude"]
# print(df[cols].median())


# describe
# print(df[cols].describe())

stats = df.agg({"latitude": ["min", "max"], "longitude": ["min", "median"]})

print(stats)
