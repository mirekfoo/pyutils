---
sidebar_label: kwargs
title: pyutils.kwargs
---

kwargs utilities.

#### getKwarg

```python
def getKwarg(kwargs, arg, default=False)
```

Retrieve a keyword argument from kwargs dict.

**Arguments**:

- `kwargs` _dict_ - The dictionary of keyword arguments.
- `arg` _str_ - The key to look for.
- `default` _any, optional_ - The default value to return if the key is not found. Defaults to False.
  

**Returns**:

- `any` - The value of the keyword argument or the default value.

