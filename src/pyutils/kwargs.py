# TODO Add metadata as in https://packaging.python.org/en/latest/specifications/core-metadata/, so it can be read with https://docs.python.org/3/library/importlib.metadata.html

"""
kwargs utilities.
"""

def getKwarg(kwargs, arg, default=False):
    """
    Retrieve a keyword argument from kwargs dict.

    Args:
        kwargs (dict): The dictionary of keyword arguments.
        arg (str): The key to look for.
        default (any, optional): The default value to return if the key is not found. Defaults to False.

    Returns:
        any: The value of the keyword argument or the default value.
    """

    return kwargs[arg] if arg in kwargs else default