# Functions

## ls02

- `pd.DataFrame()`
- `pd.Series()`
- `pandas.core.series.Series.max()`
- `pandas.core.frame.DataFrame.head()`
- `pandas.core.frame.DataFrame.tail()`
- `pandas.core.frame.DataFrame.dtypes`
- `pandas.core.frame.DataFrame.to_excel()` (required library: `python3 -m pip install openpyxl`)
- `pandas.core.frame.DataFrame.shape`
- `pandas.core.series.Series.shape`

## ls03

- `pandas.core.frame.DataFrame.sort_values(by="col_name")`
- `pandas.core.frame.DataFrame.sort_values(by="col_name", ascending=False)`
- `df["lat1"] = df["latitude"] * 2`
- `df["lat2"] = df["latitude"] / df["longitude"]`
- `pandas.core.frame.DataFrame.describe()`
- `pandas.core.frame.DataFrame.agg({"country_name": ["count"], "latitude": ["count", "mean", "min", "max"]})`
- `pandas.core.series.Series.notna()`
- `pandas.core.series.Series.fillna("something"))`
- `pandas.core.series.Series.dropna()`
