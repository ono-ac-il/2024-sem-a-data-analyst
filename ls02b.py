import pandas as pd

df_firstn = pd.read_csv("countries.csv")
# print(df_firstn.head(8))
# print(df_firstn.tail(8))

# print(df_firstn.dtypes)

# df_firstn.to_excel("a.xlsx", sheet_name="a", index=False)

dftest = pd.read_excel("a.xlsx", "a")
# print(dftest)

# print(dftest.shape)
# print(dftest["country"].shape)

# cols = ["country", "name"]
# print(dftest[cols])

subdf = dftest[dftest["latitude"] > 0]

subdf = dftest[(dftest["latitude"] > 0) & (dftest["longitude"] > 0)]

print(subdf)
