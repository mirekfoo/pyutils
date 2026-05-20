"""Configuration management utilities."""

from typing import List, Dict, Any

_addDefaults = True
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
        if _addDefaults:
            args[arg] = defval # add default value to the dictionary
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
    
    for idx, a in enumerate(arg_split):
        if isinstance(val, dict) and a in val:
            val = val[a]
            continue

        # If the path is missing, return or add the default value.
        if defval is not None:
            if _addDefaults:
                if not isinstance(val, dict):
                    raise ConfigError(
                        f"Configuration error: '{'.'.join(arg_split[:idx])}' is not a dictionary, cannot add '{arg}'."
                    )
                for missing_key in arg_split[idx:-1]:
                    val[missing_key] = {}
                    val = val[missing_key]
                val[arg_split[-1]] = defval
            return defval

        raise ConfigError(f"Configuration error: '{arg}' not defined.")

    return val
