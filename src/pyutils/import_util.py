"""Import utility functions."""

import sys, importlib

def refresh_func(func):
    """
    Refresh a function by reloading its module.
    Usage:
        func = refresh_func(func)
    """
    module = sys.modules[func.__module__]
    importlib.reload(module)
    return getattr(module, func.__name__)
