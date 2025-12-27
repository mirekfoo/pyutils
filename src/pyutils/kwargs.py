# TODO Add metadata as in https://packaging.python.org/en/latest/specifications/core-metadata/, so it can be read with https://docs.python.org/3/library/importlib.metadata.html

"""
kwargs utilities.
"""

def getKwarg(kwargs, arg, default=False):
    """Get a keyword argument from kwargs dict, return default if not found."""
    return kwargs[arg] if arg in kwargs else default