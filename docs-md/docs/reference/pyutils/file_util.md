---
sidebar_label: file_util
title: pyutils.file_util
---

File operations utilities.

#### fbak

```python
def fbak(filename: str,
         archive_subdir: str = None,
         copy: bool = False) -> None
```

Back up a file by appending an incrementing suffix to its name. If the file exists, create a backup copy of a file by appending &#x27;-i&#x27; to its name (before extension). If filename-i.ext already exists, increment i until an unused filename is found.

**Arguments**:

- `filename` _str_ - Path of the file to back up.
- `archive_subdir` _str, optional_ - Subdirectory to store the backup in.
  If provided, the subdirectory is created if it does not exist.
- `copy` _bool_ - If True, copy the file; if False, rename (move) it.

