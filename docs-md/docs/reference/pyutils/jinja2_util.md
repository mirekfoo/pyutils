---
sidebar_label: jinja2_util
title: pyutils.jinja2_util
---

Jinja2 utilities.

#### relative\_to

```python
def relative_to(master_path: str, slave_path: str) -> str
```

Calculate the relative path from master_path to slave_path.

**Arguments**:

- `master_path` - The base directory path.
- `slave_path` - The target path to make relative.
  

**Returns**:

  The relative path from master_path to slave_path.

#### setupJinja2Env

```python
def setupJinja2Env(env: Environment = None) -> Environment
```

Setup the Jinja2 environment.

**Arguments**:

- `env` - The environment to setup.
  

**Returns**:

  The setup environment.

#### expandTemplatesInStr

```python
def expandTemplatesInStr(s: str, args: Dict, env: Environment = None) -> str
```

Expand Jinja2 templates in a string using the provided arguments.

**Arguments**:

- `s` - The string containing Jinja2 templates.
- `args` - A dictionary of arguments to use for template expansion.
  

**Returns**:

  The rendered string with templates expanded.

#### expandTemplates

```python
def expandTemplates(o: Any, args: Dict, env: Environment = None) -> Any
```

Expand Jinja2 templates in an object using the provided arguments.

**Arguments**:

- `o` - The object containing Jinja2 templates.
- `args` - A dictionary of arguments to use for template expansion.
  

**Returns**:

  The rendered object with templates expanded.

