"""Pandas utility functions."""

import pandas as pd

def tuples2DF(tuples : list, columns : list = None) -> pd.DataFrame:
    """
    Converts list of tuples into Pandas DataFrame for nice viewing.

    Args:
        tuples: list of tuples.
        columns: list of column names.

    Returns:
        pd.DataFrame: A DataFrame object.
    """
    if (columns is None):
        columns = ['Key', 'Value']
    dicts = [dict(zip(columns, _tuple)) for _tuple in tuples]
    return pd.DataFrame(dicts)

def dict2DF(d : dict, columns : list = None) -> pd.DataFrame:
    """
    Converts dict into Pandas DataFrame for nice viewing.

    Args:
        d: dict.
        columns: list of column names.

    Returns:
        pd.DataFrame: A DataFrame object.
    """
    return tuples2DF(d.items(), columns)
    
    # if (columns is None):
    #     columns = ['Key', 'Value']
    # dicts = [dict(zip(columns, _tuple)) for _tuple in d.items()]
    # return pd.DataFrame(dicts)

def dicts2DF(dicts : list) -> pd.DataFrame:
    """
    Converts list of dicts into Pandas DataFrame for nice viewing.

    Args:
        dicts: list of dicts.

    Returns:
        pd.DataFrame: A DataFrame object.
    """

    if (dicts is None or len(dicts) == 0):
        return pd.DataFrame()

    columns = dicts[0].keys()

    # Construct list of tuples such that each tuple values from the dict in keys order
    tuples = [tuple(d[key] for key in columns) for d in dicts]

    return pd.DataFrame(tuples, columns=columns)
