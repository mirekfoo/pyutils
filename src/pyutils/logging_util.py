"""Redirect utility for logging module."""

from typing import IO, List

from pyutils.kwargs import getKwarg

def loggging_redirect(file : IO[str] | str, logger_names : List, **kwargs) -> None:
    """
    Redirect logging output from specified loggers to a file or stream.
    This function configures one or more loggers to output their messages to a specified
    file or stream handler. It allows customization of logging level and formatter.
    Args:
        file (IO[str] | str): Destination for log output. Can be a file path (str) or
            a file-like object (IO[str]). If a string is provided, logs are appended
            to the file at that path. If a file object is provided, logs are written
            to that stream.
        logger_names (List): List of logger names to configure. These loggers will be
            set to use the specified handler and will not propagate messages to parent
            loggers.
        **kwargs: Optional keyword arguments:
            - level (int): Logging level for the handler and loggers. 
              Defaults to logging.INFO.
            - formatter (logging.Formatter): Custom formatter for log messages.
              If None, no formatter is applied. Defaults to None.
    Returns:
        None
    Example:
        >>> loggging_redirect('app.log', ['myapp', 'myapp.module'], level=logging.DEBUG)
        >>> loggging_redirect(sys.stdout, ['myapp'], formatter=logging.Formatter("%(name)s: %(message)s"))
    """

    import logging

    level = getKwarg(kwargs, 'level', logging.INFO)
    formatter = getKwarg(kwargs, 'formatter', None)

    if isinstance(file, str):
        handler = logging.FileHandler(file, mode="a")
    else:
        handler = logging.StreamHandler(file)

    handler.setLevel(level)

    # formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
    if formatter:
        handler.setFormatter(formatter)

    for name in logger_names:
        logger = logging.getLogger(name)
        logger.setLevel(level)
        logger.addHandler(handler)
        logger.propagate = False
