---
sidebar_label: tool_util
title: pyutils.tool_util
---

CLI Tool utilities.
This module provides basic utilities for command-line tools, including:
    - Command line invocation
    - Home directory path
    - Command-line arguments
    - Tool name
    - Usage information callback

Functions:
    getCmd() -&gt; str: Returns the full command line invocation.
    getHomeDir() -&gt; str: Returns the tool&#x27;s home directory.
    getArgV() -&gt; list: Returns the command-line arguments.
    setUsagePrintProc(p: callable) -&gt; None: Sets the callback for printing usage.
    printUsage() -&gt; None: Invokes the usage print callback if set.
    setToolShortName(name: str) -&gt; None: Sets the tool&#x27;s short name.
    getToolShortName() -&gt; str: Returns the tool&#x27;s short name.

#### getCmd

```python
def getCmd()
```

Retrieve the global command variable.

**Returns**:

  The current value of the global cmd variable.

#### getHomeDir

```python
def getHomeDir()
```

Retrieve the home directory path.
This function returns the global home_dir variable that contains
the path to the user&#x27;s home directory.

**Returns**:

- `str` - The path to the home directory.

#### getArgV

```python
def getArgV()
```

Retrieve the global command-line arguments list.

**Returns**:

- `list` - The global argv variable containing command-line arguments.

#### setUsagePrintProc

```python
def setUsagePrintProc(p)
```

Set the global usage print procedure.
This function allows you to configure a custom procedure that will be called
to print usage information. The provided procedure replaces the default usage
printing behavior.

**Arguments**:

- `p` - A callable that implements the usage printing logic. This procedure
  will be invoked whenever usage information needs to be displayed.
  

**Returns**:

  None

#### printUsage

```python
def printUsage()
```

Print the usage information for the application.
Retrieves and executes the global usage function if it has been defined.
This function serves as a wrapper to display usage/help information to the user.

**Raises**:

- `NameError` - If the global &#x27;usage&#x27; variable has not been defined before calling this function.

#### setToolShortName

```python
def setToolShortName(name)
```

Set the global tool variable to the provided short name.

**Arguments**:

- `name` _str_ - The short name to assign to the global tool variable.
  

**Returns**:

  None

#### getToolShortName

```python
def getToolShortName()
```

Get the short name of the current tool.

**Returns**:

- `str` - The short name of the tool if it is set, otherwise returns an empty string.

