---
sidebar_label: pandas_util
title: pyutils.pandas_util
---

Pandas utility functions.

#### tuples2DF

```python
def tuples2DF(tuples: list, columns: list = None) -> pd.DataFrame
```

Converts list of tuples into Pandas DataFrame for nice viewing.

**Arguments**:

- `tuples` - list of tuples.
- `columns` - list of column names.
  

**Returns**:

- `pd.DataFrame` - A DataFrame object.

#### dict2DF

```python
def dict2DF(d: dict, columns: list = None) -> pd.DataFrame
```

Converts dict into Pandas DataFrame for nice viewing.

**Arguments**:

- `d` - dict.
- `columns` - list of column names.
  

**Returns**:

- `pd.DataFrame` - A DataFrame object.

#### dicts2DF

```python
def dicts2DF(dicts: list) -> pd.DataFrame
```

Converts list of dicts into Pandas DataFrame for nice viewing.

**Arguments**:

- `dicts` - list of dicts.
  

**Returns**:

- `pd.DataFrame` - A DataFrame object.

