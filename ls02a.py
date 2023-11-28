import pandas as pd

# Pandas datatype is Dataframe
df = pd.DataFrame(
    {
        "CountryName": ["Sweden", "Israel", "Indonesia"],
        "CountryCode": ["02", "972", "67"],
        "CapitalCity": ["Stokholm", "Jerusalem", "Jakarta"],
    }
)
# print(type(df))  # pandas.core.frame.DataFrame


# Every column is Series
# print(type(df["CapitalCity"]))  # pandas.core.series.Series

series1 = pd.Series(["Sweden", "Israel", "Indonesia"])
series2 = pd.Series([2, 972, 67])
series3 = pd.Series(["Stokholm", "Jerusalem", "Jakarta"])

df2 = pd.DataFrame(
    {
        "CountryName": series1,
        "CountryCode": series2,
        "CapitalCity": series3,
    }
)
# print(df2)

# print(df2["CountryCode"].max())
# print(series2.max())
print(df.describe())

# df_firstn = pd.read_csv("countries.csv", nrows=1)
# print(df_firstn)
