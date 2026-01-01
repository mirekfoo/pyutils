"""Configuration management utilities."""

from typing import List, Dict, Any

class ConfigError(Exception):
    """Exception raised for errors in the configuration."""
    pass

def read_config_arg(args: Dict, arg: str, defval: Any) -> Any:
    """
    Read a configuration argument from a dictionary.

    Args:
        args: The dictionary containing configuration arguments.
        arg: The key to look for in the dictionary.
        defval: The default value to return if the key is not found. If None, the argument is required.

    Returns:
        The value associated with the key or the default value.
    """

    if arg in args:
        return args[arg]
    elif defval is not None:
        return defval
    else:
        raise ConfigError(f"Configuration error: '{arg}' not defined.")

def read_config_harg(args: Dict, arg: str, defval: Any) -> Any:
    """
    Read a hierarchical configuration argument from a dictionary.

    Args:
        args: The dictionary containing configuration arguments.
        arg: The dot-separated key to look for in the dictionary.
        defval: The default value to return if the key is not found. If None, the argument is required.

    Returns:
        The value associated with the key or the default value.
    """

    val = args
    arg_split = arg.split(".")
    
    for a in arg_split:
        if a in val:
            val = val[a]
        else:
            val = None
            break

    if val is not None:
        return val
    elif defval is not None:
        return defval
    else:
        raise ConfigError(f"Configuration error: '{arg}' not defined.")
