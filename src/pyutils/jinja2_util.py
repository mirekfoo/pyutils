"""Jinja2 utilities."""

from typing import List, Dict, Any
from jinja2 import Template, Environment

jinja2_env = None

def expandTemplatesInStr(s: str, args: Dict, env: Environment = None) -> str:
    """
    Expand Jinja2 templates in a string using the provided arguments.

    Args:
        s: The string containing Jinja2 templates.
        args: A dictionary of arguments to use for template expansion.

    Returns:
        The rendered string with templates expanded.
    """

    global jinja2_env

    if env is None:
        if jinja2_env is None:
            jinja2_env = Environment()
        env = jinja2_env

    return env.from_string(s).render(args)

def expandTemplates(o: Any, args: Dict, env: Environment = None) -> Any:
    """
    Expand Jinja2 templates in an object using the provided arguments.

    Args:
        o: The object containing Jinja2 templates.
        args: A dictionary of arguments to use for template expansion.

    Returns:
        The rendered object with templates expanded.
    """
    if isinstance(o, str):
        return expandTemplatesInStr(o, args, env)
    elif isinstance(o, list):
        return [expandTemplates(s, args, env) for s in o]
    elif isinstance(o, dict):
        return {k: expandTemplates(v, args, env) for k, v in o.items()}
    else:
        return o
