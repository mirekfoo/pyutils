import os
import __main__

import utils.file_util
from utils.kwargs import getKwarg

class FileLogger:

    def __init__(self, **kwargs) -> None:
        
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
            utils.file_util.fbak(self.LOG_FILE_NAME, archive_subdir=self.ARCHIVE_DIR)
            self.FILE = open(self.LOG_FILE_NAME, "a", encoding="utf-8")

            # redirect stdout and stderr to log file
            #sys.stdout = log_file
            #sys.stderr = log_file

    # -----------------------------------------------------------------

    def print(self, s : str, **kwargs) -> None:
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
        kwargs['echo'] = True
        self.print(s, **kwargs)

    # -----------------------------------------------------------------

    def close(self) -> None:
        if self.FILE:
            self.FILE.close()
            utils.file_util.fbak(self.LOG_FILE_NAME, archive_subdir=self.ARCHIVE_DIR)

    # -----------------------------------------------------------------
            
