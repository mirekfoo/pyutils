---
sidebar_label: config_util
title: pyutils.config_util
---

Configuration management utilities.

## ConfigError Objects

```python
class ConfigError(Exception)
```

Exception raised for errors in the configuration.

#### read\_config\_arg

```python
def read_config_arg(args: Dict, arg: str, defval: Any) -> Any
```

Read a configuration argument from a dictionary.

**Arguments**:

- `args` - The dictionary containing configuration arguments.
- `arg` - The key to look for in the dictionary.
- `defval` - The default value to return if the key is not found. If None, the argument is required.
  

**Returns**:

  The value associated with the key or the default value.

#### read\_config\_harg

```python
def read_config_harg(args: Dict, arg: str, defval: Any) -> Any
```

Read a hierarchical configuration argument from a dictionary.

**Arguments**:

- `args` - The dictionary containing configuration arguments.
- `arg` - The dot-separated key to look for in the dictionary.
- `defval` - The default value to return if the key is not found. If None, the argument is required.
  

**Returns**:

  The value associated with the key or the default value.

