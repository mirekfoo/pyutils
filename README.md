# Python Utilities Collection

`pyutils` is a collection of handy routines and classes for Python apps.

# Documentation

Docs|
---|
[Markdown docs](docs-md/docs/index.md)
[Web docs](https://mirekfoo.github.io/pyutils/api/)

# Usage

## Install in client project

### pip direct install

```bash
pip install git+https://github.com/mirekfoo/pyutils.git
```

### pip install from pyproject.toml

* `pyproject.toml`:
```toml
[project]
dependencies = [    
    "pyutils @ git+https://github.com/mirekfoo/pyutils.git"
]
```

```bash
pip install .
```

## Install as editable dependency

```bash
git clone https://github.com/mirekfoo/pyutils.git
pip install -e pyutils
```

# Development

* Type `make help` for available **dev** procedures
