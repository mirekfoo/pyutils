"""Jinja2 utilities."""

from pathlib import Path
from typing import List, Dict, Any
from jinja2 import Template, Environment

jinja2_env = None

def relative_to(master_path: str, slave_path: str) -> str:
    """
    Calculate the relative path from master_path to slave_path.

    Args:
        master_path: The base directory path.
        slave_path: The target path to make relative.

    Returns:
        The relative path from master_path to slave_path.
    """
    
    rel_path =  Path(slave_path).relative_to(master_path, walk_up=True)
    return rel_path

def setupJinja2Env(env: Environment = None) -> Environment:
    """
    Setup the Jinja2 environment.

    Args:
        env: The environment to setup.

    Returns:
        The setup environment.
    """

    global jinja2_env
    
    if env is None:
        if jinja2_env is None:
            jinja2_env = Environment()
            jinja2_env.globals["relative_to"] = relative_to
        env = jinja2_env
    return env

def expandTemplatesInStr(s: str, args: Dict, env: Environment = None) -> str:
    """
    Expand Jinja2 templates in a string using the provided arguments.

    Args:
        s: The string containing Jinja2 templates.
        args: A dictionary of arguments to use for template expansion.

    Returns:
        The rendered string with templates expanded.
    """

    return setupJinja2Env(env).from_string(s).render(args)

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
