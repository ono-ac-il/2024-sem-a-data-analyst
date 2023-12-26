# Functions

## Extras

### Remove '/' from column names and trim spaces

`pandas.core.frame.DataFrame.columns.str.replace('/', '', regex=False).str.strip()`

### Remove '/' and trim spaces of data rows

```python
for col in pandas.core.frame.DataFrame.select_dtypes(include=[object]):
    pandas.core.frame.DataFrame[col] = pandas.core.frame.DataFrame[col].astype(str).str.replace('/', '', regex=False).str.strip()
```

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
- `pd.concat([pandas.core.frame.DataFrame, pandas.core.frame.DataFrame])`

## ls04

- rename column: `pandas.core.frame.DataFrame.rename(columns={'colnam': 'new_colname'}, inplace=True)`
- convert to number: `pandas.core.frame.DataFrame["colname"] = pd.to_numeric(pandas.core.frame.DataFrame["colname"], errors='coerce')`
- Get next row column value into new column: `pandas.core.frame.DataFrame['new_clo'] = pandas.core.frame.DataFrame['col'].shift(-1)`
- Merge dataframes with speicific columns: `pd.merge(pandas.core.frame.DataFrame, pandas.core.frame.DataFrame[['col1', 'col2']], on='col1', how='left')
`
