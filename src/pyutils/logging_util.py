from typing import IO, List

from utils.kwargs import getKwarg

def loggging_redirect(file : IO[str] | str, logger_names : List, **kwargs) -> None:

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
