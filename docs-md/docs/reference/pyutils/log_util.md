---
sidebar_label: log_util
title: pyutils.log_util
---

FileLogger class for managing file-based logging with archiving logs from previous runs.

## FileLogger Objects

```python
class FileLogger()
```

FileLogger class for managing file-based logging with archiving logs from previous runs.
This class provides functionality to log messages to a file with support for
archiving previous log files and optional console output.

**Attributes**:

- `ARCHIVE_DIR` _str_ - Directory where archived log files are stored.
- `LOG_FILE_NAME` _str_ - Full path to the log file.
- `FILE` _file object_ - Open file handle for writing logs, or None if not initialized.
  

**Methods**:

  
- `__init__(**kwargs)` - Initialize the FileLogger with configuration parameters.
  

**Arguments**:

- `logDir` _str, optional_ - Directory where log file is created. Defaults to the directory of __main__.
- `logArchiveDir` _str, optional_ - Subdirectory for archived logs. Defaults to &#x27;archive&#x27;.
- `logBaseName` _str, optional_ - Base name for the log file. Defaults to the name of __main__.
- `logNameSuffix` _str, optional_ - Suffix to append to log file name. Defaults to None.
- `logExt` _str, optional_ - File extension for log file. Defaults to &#x27;.log&#x27;.
  
- `print(s` - str, **kwargs): Write a message to the log file.
  

**Arguments**:

- `LOG_FILE_NAME`0 _str_ - Message to log.
- `LOG_FILE_NAME`1 _bool, optional_ - If True, also print to console. Defaults to False.
- `LOG_FILE_NAME`2 _bool, optional_ - If True, format as a section header. Defaults to False.
- `LOG_FILE_NAME`3 _int, optional_ - Width of section header. Defaults to 80.
- `LOG_FILE_NAME`4 _str, optional_ - Character to fill section header. Defaults to &#x27;=&#x27;.
  
- `LOG_FILE_NAME`5 - str, **kwargs): Write a message to both log file and console.
  

**Arguments**:

- `LOG_FILE_NAME`0 _str_ - Message to log and print.
- `LOG_FILE_NAME`7 - Additional arguments passed to print().
  
- `LOG_FILE_NAME`8 - Close the log file and archive it.

#### \_\_init\_\_

```python
def __init__(**kwargs) -> None
```

Initialize the logger with configurable log directory and file settings.

**Arguments**:

- `**kwargs` - Arbitrary keyword arguments:
- `logDir` _str, optional_ - Directory where log files are stored.
  Defaults to the directory of the main module.
- `logArchiveDir` _str, optional_ - Subdirectory for archived log files.
  Defaults to &#x27;archive&#x27;.
- `logBaseName` _str, optional_ - Base name for the log file.
  Defaults to the name of the main module file (without extension).
- `logNameSuffix` _str, optional_ - Suffix to append to the log file name.
  Defaults to None.
- `logExt` _str, optional_ - File extension for the log file.
  Defaults to &#x27;.log&#x27;.
  

**Returns**:

  None
  

**Attributes**:

- `ARCHIVE_DIR` _str_ - Directory path for archived log files.
- `LOG_FILE_NAME` _str_ - Full path to the log file.
- `FILE` _file object_ - File handle for writing to the log file, or None if
  LOG_FILE_NAME is not set.
  

**Notes**:

  - Creates a backup of the existing log file using fbak() and archives it.
  - Opens the log file in append mode with UTF-8 encoding.

#### print

```python
def print(s: str, **kwargs) -> None
```

Print a message to file and/or console.

**Arguments**:

- `s` _str_ - The message string to print.
- `**kwargs` - Optional keyword arguments:
- `echo` _bool, optional_ - If True, also print to console. Defaults to False.
- `section` _bool, optional_ - If True, format the message as a section header. Defaults to False.
- `sectionWidth` _int, optional_ - Width of the section header. Defaults to 80.
- `sectionFillChar` _str, optional_ - Character to use for filling the section header. Defaults to &#x27;=&#x27;.
  

**Returns**:

  None

#### echo

```python
def echo(s: str, **kwargs)
```

Print a string to the console and log it.

**Arguments**:

- `s` _str_ - The string to print and log.
- `**kwargs` - Additional keyword arguments to pass to the print method.
  The &#x27;echo&#x27; parameter will be set to True automatically.

#### close

```python
def close() -> None
```

Close the file handler and archive the log file.
Closes the currently open log file if it exists and creates a backup
archive of the log file in the designated archive directory.

**Raises**:

  None
  

**Returns**:

  None

