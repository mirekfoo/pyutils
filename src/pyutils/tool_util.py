
# TODO Add metadata as in https://packaging.python.org/en/latest/specifications/core-metadata/, so it can be read with https://docs.python.org/3/library/importlib.metadata.html

"""CLI Tool utilities.
This module provides basic utilities for command-line tools, including:
    - Command line invocation
    - Home directory path
    - Command-line arguments
    - Tool name
    - Usage information callback

Functions:
    getCmd() -> str: Returns the full command line invocation.
    getHomeDir() -> str: Returns the tool's home directory.
    getArgV() -> list: Returns the command-line arguments.
    setUsagePrintProc(p: callable) -> None: Sets the callback for printing usage.
    printUsage() -> None: Invokes the usage print callback if set.
    setToolShortName(name: str) -> None: Sets the tool's short name.
    getToolShortName() -> str: Returns the tool's short name.
"""

cmd = None
home_dir = None
argv = None
usage = None
tool = None
 
def getCmd():
    """
    Retrieve the global command variable.

    Returns:
        The current value of the global cmd variable.
    """
    
    global cmd
    return cmd
 
def getHomeDir():
    """
    Retrieve the home directory path.
    This function returns the global home_dir variable that contains
    the path to the user's home directory.

    Returns:
        str: The path to the home directory.
    """

    global home_dir
    return home_dir
 
def getArgV():
    """
    Retrieve the global command-line arguments list.

    Returns:
        list: The global argv variable containing command-line arguments.
    """

    global argv
    return argv
 
def setUsagePrintProc(p):
    """
    Set the global usage print procedure.
    This function allows you to configure a custom procedure that will be called
    to print usage information. The provided procedure replaces the default usage
    printing behavior.

    Args:
        p: A callable that implements the usage printing logic. This procedure
           will be invoked whenever usage information needs to be displayed.

    Returns:
        None
    """
    
    global usage
    usage = p
 
def printUsage():
    """
    Print the usage information for the application.
    Retrieves and executes the global usage function if it has been defined.
    This function serves as a wrapper to display usage/help information to the user.

    Raises:
        NameError: If the global 'usage' variable has not been defined before calling this function.
    """
    
    global usage
    if usage:
        usage()
 
def setToolShortName(name):
    """
    Set the global tool variable to the provided short name.

    Args:
        name (str): The short name to assign to the global tool variable.

    Returns:
        None
    """
    
    global tool
    tool = name
 
def getToolShortName():
    """
    Get the short name of the current tool.

    Returns:
        str: The short name of the tool if it is set, otherwise returns an empty string.
    """

    global tool
    return tool if tool else ''
 
# -----------------------------
 
import os
import sys
 
cmd = ' '.join(sys.argv)
home_dir = os.path.dirname(sys.argv[0])
argv = sys.argv[1:]
setToolShortName(os.path.splitext(os.path.basename(sys.argv[0]))[0])
 

 
