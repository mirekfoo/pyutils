"""FileLogger class for managing file-based logging with archiving logs from previous runs."""

import os
import __main__

import pyutils.file_util
from pyutils.kwargs import getKwarg

class FileLogger:
    """
    FileLogger class for managing file-based logging with archiving logs from previous runs.
    This class provides functionality to log messages to a file with support for
    archiving previous log files and optional console output.

    Attributes:
        ARCHIVE_DIR (str): Directory where archived log files are stored.
        LOG_FILE_NAME (str): Full path to the log file.
        FILE (file object): Open file handle for writing logs, or None if not initialized.

    Methods:

        __init__(**kwargs): Initialize the FileLogger with configuration parameters.

            Args:
                logDir (str, optional): Directory where log file is created. Defaults to the directory of __main__.
                logArchiveDir (str, optional): Subdirectory for archived logs. Defaults to 'archive'.
                logBaseName (str, optional): Base name for the log file. Defaults to the name of __main__.
                logNameSuffix (str, optional): Suffix to append to log file name. Defaults to None.
                logExt (str, optional): File extension for log file. Defaults to '.log'.

        print(s: str, **kwargs): Write a message to the log file.

            Args:
                s (str): Message to log.
                echo (bool, optional): If True, also print to console. Defaults to False.
                section (bool, optional): If True, format as a section header. Defaults to False.
                sectionWidth (int, optional): Width of section header. Defaults to 80.
                sectionFillChar (str, optional): Character to fill section header. Defaults to '='.

        echo(s: str, **kwargs): Write a message to both log file and console.

            Args:
                s (str): Message to log and print.
                **kwargs: Additional arguments passed to print().

        close(): Close the log file and archive it.
    """

    def __init__(self, **kwargs) -> None:
        """
        Initialize the logger with configurable log directory and file settings.

        Args:
            **kwargs: Arbitrary keyword arguments:
                logDir (str, optional): Directory where log files are stored. 
                    Defaults to the directory of the main module.
                logArchiveDir (str, optional): Subdirectory for archived log files. 
                    Defaults to 'archive'.
                logBaseName (str, optional): Base name for the log file. 
                    Defaults to the name of the main module file (without extension).
                logNameSuffix (str, optional): Suffix to append to the log file name. 
                    Defaults to None.
                logExt (str, optional): File extension for the log file. 
                    Defaults to '.log'.

        Returns:
            None

        Attributes:
            ARCHIVE_DIR (str): Directory path for archived log files.
            LOG_FILE_NAME (str): Full path to the log file.
            FILE (file object): File handle for writing to the log file, or None if 
                LOG_FILE_NAME is not set.

        Note:
            - Creates a backup of the existing log file using fbak() and archives it.
            - Opens the log file in append mode with UTF-8 encoding.
        """
        
        logDir = getKwarg(kwargs, 'logDir', None)
        logArchiveDir = getKwarg(kwargs, 'logArchiveDir', 'archive')
        logBaseName = getKwarg(kwargs, 'logBaseName', None)
        logNameSuffix = getKwarg(kwargs, 'logNameSuffix', None)
        logExt = getKwarg(kwargs, 'logExt', '.log')

        if not logDir:
            logDir = os.path.dirname(__main__.__file__)
        if not logBaseName:
            logBaseName =  os.path.splitext(os.path.basename(__main__.__file__))[0]

        self.ARCHIVE_DIR = logArchiveDir 
        self.LOG_FILE_NAME = os.path.join(logDir, logBaseName + (logNameSuffix if logNameSuffix else '') + logExt)
        self.FILE = None

        if self.LOG_FILE_NAME:
            pyutils.file_util.fbak(self.LOG_FILE_NAME, archive_subdir=self.ARCHIVE_DIR)
            self.FILE = open(self.LOG_FILE_NAME, "a", encoding="utf-8")

            # redirect stdout and stderr to log file
            #sys.stdout = log_file
            #sys.stderr = log_file

    # -----------------------------------------------------------------

    def print(self, s : str, **kwargs) -> None:
        """
        Print a message to file and/or console.

        Args:
            s (str): The message string to print.
            **kwargs: Optional keyword arguments:
                echo (bool, optional): If True, also print to console. Defaults to False.
                section (bool, optional): If True, format the message as a section header. Defaults to False.
                sectionWidth (int, optional): Width of the section header. Defaults to 80.
                sectionFillChar (str, optional): Character to use for filling the section header. Defaults to '='.

        Returns:
            None
        """

        echo = getKwarg(kwargs, 'echo', False)
        section = getKwarg(kwargs, 'section', False)

        if section:
            sectionWidth = getKwarg(kwargs, 'sectionWidth', 80)
            sectionFillChar = getKwarg(kwargs, 'sectionFillChar', '=')

            s = ' ' + s + ' '
            s = s.center(sectionWidth, sectionFillChar)

        if self.FILE:
            print(s, file=self.FILE)
        if echo:
            print(s)

    def echo(self, s : str, **kwargs):
        """
        Print a string to the console and log it.

        Args:
            s (str): The string to print and log.
            **kwargs: Additional keyword arguments to pass to the print method.
                     The 'echo' parameter will be set to True automatically.
        """

        kwargs['echo'] = True
        self.print(s, **kwargs)

    # -----------------------------------------------------------------

    def close(self) -> None:
        """
        Close the file handler and archive the log file.
        Closes the currently open log file if it exists and creates a backup
        archive of the log file in the designated archive directory.

        Raises:
            None

        Returns:
            None
        """

        if self.FILE:
            self.FILE.close()
            pyutils.file_util.fbak(self.LOG_FILE_NAME, archive_subdir=self.ARCHIVE_DIR)

    # -----------------------------------------------------------------
            
