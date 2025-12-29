---
sidebar_label: logging_util
title: pyutils.logging_util
---

Redirect utility for logging module.

#### loggging\_redirect

```python
def loggging_redirect(file: IO[str] | str, logger_names: List,
                      **kwargs) -> None
```

Redirect logging output from specified loggers to a file or stream.
This function configures one or more loggers to output their messages to a specified
file or stream handler. It allows customization of logging level and formatter.

**Arguments**:

- `file` _IO[str] | str_ - Destination for log output. Can be a file path (str) or
  a file-like object (IO[str]). If a string is provided, logs are appended
  to the file at that path. If a file object is provided, logs are written
  to that stream.
- `logger_names` _List_ - List of logger names to configure. These loggers will be
  set to use the specified handler and will not propagate messages to parent
  loggers.
- `**kwargs` - Optional keyword arguments:
  - level (int): Logging level for the handler and loggers.
  Defaults to logging.INFO.
  - formatter (logging.Formatter): Custom formatter for log messages.
  If None, no formatter is applied. Defaults to None.
  

**Returns**:

  None
  

**Examples**:

  &gt;&gt;&gt; loggging_redirect(&#x27;app.log&#x27;, [&#x27;myapp&#x27;, &#x27;myapp.module&#x27;], level=logging.DEBUG)
  &gt;&gt;&gt; loggging_redirect(sys.stdout, [&#x27;myapp&#x27;], formatter=logging.Formatter(&quot;%(name)s: %(message)s&quot;))

