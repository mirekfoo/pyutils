"""Pandas utility functions."""
import pandas as pd

def tuples2DF(tuples : list, columns) -> pd.DataFrame:
    """
    Converts list of tuples into Pandas DataFrame for nice viewing.

    Args:
        tuples: list of tuples.

    Returns:
        pd.DataFrame: A DataFrame object.
    """
    if (columns is None):
        columns = ['Key', 'Value']
    dicts = [dict(zip(columns, _tuple)) for _tuple in tuples]
    return pd.DataFrame(dicts)

def dict2DF(d : dict, columns) -> pd.DataFrame:
    """
    Converts dict into Pandas DataFrame for nice viewing.

    Args:
        d: dict.

    Returns:
        pd.DataFrame: A DataFrame object.
    """
    tuples2DF(d.items(), columns)
    
    # if (columns is None):
    #     columns = ['Key', 'Value']
    # dicts = [dict(zip(columns, _tuple)) for _tuple in d.items()]
    # return pd.DataFrame(dicts)
