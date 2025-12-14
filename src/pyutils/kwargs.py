# TODO Add metadata as in https://packaging.python.org/en/latest/specifications/core-metadata/, so it can be read with https://docs.python.org/3/library/importlib.metadata.html

"""
kwargs utilities.
"""

def getKwarg(kwargs, arg, default=False):
    return kwargs[arg] if arg in kwargs else default