"""JSON formatting utilities.
JSON formatting utilities for converting Python objects to JSON strings with customizable formatting.
This module provides functions to serialize Python objects, dictionaries, and lists to JSON format
with support for:
- Custom indentation and base indentation levels
- String truncation for long values
- Template-based filtering of dictionary properties
- Regex pattern matching for dynamic property selection
- Pydantic model serialization
Key Functions:
- obj2JSON: Convert objects to JSON-serializable format
- as_json: Convert objects to formatted JSON strings with indentation control
- as_json_str_truncated: Convert objects to JSON with optional string truncation
- dict_as_json: Convert dictionaries to JSON with template-based filtering
- list_as_json: Convert lists to formatted JSON arrays
- patterns_from_template: Extract regex patterns from template dictionaries
- find_match_in_template: Search for exact or pattern matches in templates
Dependencies:
- typing: Type hints
- json: JSON serialization
- re: Regular expression pattern matching
- pyutils.str_util: String utility functions
- pyutils.kwargs: Keyword argument extraction
"""

from typing import Any, Dict, List, Optional
import json
import re

from pyutils.str_util import truncate_string
from pyutils.kwargs import getKwarg

def obj2JSON(obj):
    """Helper function to convert objects to JSON-serializable format."""
    try:
        return obj.model_dump()
    except Exception:
        return str(obj)

#def as_json(obj, indent=2) -> str:
def as_json(obj, **kwargs) -> str:
    """
    Convert a Python object to a JSON string with customizable indentation.
    Args:
        obj: The Python object to be converted to JSON format.
        **kwargs: Optional keyword arguments:
            - base_indent (int): The base indentation level (number of spaces) to apply 
              to all lines. Default is 0.
            - indent (int): The number of spaces per indentation level. Default is 2.
    Returns:
        str: A JSON-formatted string representation of the input object.
    Notes:
        - Uses json.dumps() with a custom obj2JSON serializer for handling non-standard types.
        - If base_indent is greater than 0, all indentation in the output is adjusted 
          by adding base_indent spaces to each indented line.
    """

    base_indent = getKwarg(kwargs, 'base_indent', 0)
    indent = getKwarg(kwargs, 'indent', 2)

    json_str =  json.dumps(obj, indent=indent, default=obj2JSON)
    if base_indent>0:
        json_str = json_str.replace(f"\n{' '*indent}",f"\n{' '*(base_indent+indent)}")
        new_line_only_re = r"\n([^\s\n])"
        new_line_only_base_indent_re = rf"\n{' '*(base_indent)}\1"
        json_str = re.sub(new_line_only_re, new_line_only_base_indent_re, json_str)
    return json_str

def as_json_str_truncated(obj,  **kwargs) -> str:
    def as_json_str_truncated(obj, **kwargs) -> str:
        """
        Convert an object to a JSON string representation with optional truncation of string values.
        Args:
            obj: The object to convert to JSON string format.
            **kwargs: Arbitrary keyword arguments including:
                base_indent (int): Base indentation level for JSON formatting. Default is 0.
                indent (int): Number of spaces per indentation level. Default is 2.
                str_limit (int, optional): Maximum length for string values. If specified and greater than 0,
                                           strings will be truncated to this length. Default is None.
        Returns:
            str: JSON string representation of the object. If the object is a string and str_limit is set,
                 the string will be truncated to the specified limit. Otherwise, the object is converted
                 to JSON using standard formatting with the specified indentation.
        """

    base_indent = getKwarg(kwargs, 'base_indent', 0)
    indent = getKwarg(kwargs, 'indent', 2)
    str_limit = getKwarg(kwargs, 'str_limit', None)

    if isinstance(obj, str):
        if str_limit and str_limit>0:
            # if not isinstance(obj, str):
            #     raise TypeError("'obj' must be a str")
            #json_str = f"[{len(obj)} chars]\"{truncate_string(obj, str_limit)}\""
            json_str = f"\"{truncate_string(obj, str_limit)}\""
            return json_str
        # else:
        #     #json_str = f"{as_json(obj, base_indent = base_indent + indent, indent = indent)}"

    json_str = as_json(obj, base_indent = base_indent + indent, indent = indent)
    return json_str


def patterns_from_template(template: Dict) -> Dict:
    """
    Extract regex patterns from a template dictionary.
    Filters a template dictionary and returns only the entries where the key
    is a compiled regular expression pattern (re.Pattern object).
    Args:
        template (Dict): A dictionary that may contain re.Pattern objects as keys.
    Returns:
        Dict: A new dictionary containing only the key-value pairs where the key
              is a re.Pattern object.
    Example:
        >>> import re
        >>> template = {
        ...     re.compile(r'\\d+'): 'number',
        ...     'name': 'value',
        ...     re.compile(r'[a-z]+'): 'letters'
        ... }
        >>> result = patterns_from_template(template)
        >>> len(result)
        2
    """

    patterns = {}
    for key in template:
        if isinstance(key, re.Pattern):
            patterns[key] = template[key]

    return patterns 

def find_match_in_template(template: Dict, dict_item: str, patterns: Dict = None) -> (bool, Any):
    """
    Search for a match of dict_item in template or patterns.
    First attempts to find an exact match of dict_item as a key in the template dictionary.
    If no exact match is found and patterns are provided, performs regex pattern matching
    against dict_item using the patterns dictionary keys.
    Args:
        template (Dict): Dictionary to search for exact key match.
        dict_item (str): The key/string to search for in template or match against patterns.
        patterns (Dict, optional): Dictionary where keys are regex patterns to match against dict_item.
            Defaults to None.
    Returns:
        tuple: A tuple of (bool, Any) where:
            - bool: True if a match is found (exact or pattern), False otherwise.
            - Any: The value from template or patterns if match is found, None otherwise.
    Examples:
        >>> template = {"key1": "value1", "key2": "value2"}
        >>> find_match_in_template(template, "key1")
        (True, "value1")
        >>> patterns = {r"key\d": "numeric_value"}
        >>> find_match_in_template(template, "key5", patterns)
        (True, "numeric_value")
        >>> find_match_in_template(template, "unknown")
        (False, None)
    """

    if dict_item in template:
        return (True, template[dict_item])

    if patterns:
        for pattern in patterns:
            if re.fullmatch(pattern, dict_item):
                return (True, patterns[pattern])

    return (False, None)

def dict_as_json(obj: Dict, **kwargs) -> str:
    """
    Convert a dictionary or Pydantic model to a formatted JSON string with optional filtering and truncation.
    Args:
        obj (Dict): A dictionary or Pydantic model object to convert to JSON string.
        **kwargs: Optional keyword arguments:
            - template (dict, optional): A dictionary specifying which properties to include and their string length limits.
              Keys are property names, values are character limits for that property's string representation.
              Defaults to None (all properties included).
            - base_indent (int, optional): Base indentation level in spaces. Defaults to 0.
            - indent (int, optional): Indentation step size in spaces. Defaults to 2.
    Returns:
        str: A formatted JSON string representation of the object. Properties not included in the template
             are hidden and their count is noted in a comment.
    Raises:
        TypeError: If obj is neither a dict nor has a model_dump() method, or if the resulting object is not a dict.
    Notes:
        - Properties matching the template are included with specified string length limits.
        - Non-matching properties are excluded and counted in a comment at the end.
        - The output uses indentation for readability when indent > 0.
        - If no properties match the template, only "{}" is returned.
    """

    template = getKwarg(kwargs, 'template', None)
    base_indent = getKwarg(kwargs, 'base_indent', 0)
    indent = getKwarg(kwargs, 'indent', 2)

    if isinstance(obj, dict):
        dict_obj = obj
    else:
        dict_obj = obj.model_dump()
    if not isinstance(dict_obj, dict):
        raise TypeError("'obj' must be a dict")

    patterns = patterns_from_template(template)

    json_str = "{"
    first = True
    match_cnt = 0
    hidden_props = []
    for dict_item in dict_obj:
        #if dict_item in template:
        match, limit = find_match_in_template(template, dict_item, patterns)
        if match:
            match_cnt += 1
            limit = template[dict_item]
            if first:
                first = False
            else:
                json_str += ","
            if indent:
                json_str += f"\n{' '*(base_indent+indent)}"
            json_str += f"\"{dict_item}\": "

            item_value = dict_obj[dict_item]
            json_str += as_json_str_truncated(item_value, base_indent = base_indent + indent, indent = indent, str_limit = limit)
        else:
            hidden_props.append(dict_item)
    hidden = len(dict_obj) - match_cnt
    if hidden>0:
        json_str += f"\n{' '*(base_indent + indent)}// {hidden} properties hidden {hidden_props}"
        first = False

    if first:                
        json_str += "}"
    else:
        json_str += f"\n{' '*base_indent}}}"
    return json_str

def list_as_json(l: List, **kwargs) -> str:
    """
    Convert a list to a formatted JSON string representation.
    Args:
        l (List): The list to convert to JSON format. Can be None or a non-list object.
        **kwargs: Optional keyword arguments:
            - to_json (callable): Custom function to convert objects to JSON strings.
              Default: as_json with specified indentation.
              Signature: to_json(obj, base_indent, indent) -> str
            - base_indent (int): Base indentation level in spaces. Default: 0
            - indent (int): Indentation increment in spaces. Default: 2
    Returns:
        str: A formatted JSON string representation of the input.
             - Returns "None" if input is None.
             - If input is not a list, returns the JSON representation of that object.
             - If input is a list, returns a bracketed JSON array with proper formatting
               and indentation.
    Example:
        >>> list_as_json([1, 2, 3])
        '[\\n  1,\\n  2,\\n  3\\n]'
        >>> list_as_json(None)
        'None'
        >>> list_as_json(42)
        '42'
    """

    to_json = getKwarg(kwargs, 'to_json', lambda obj, base_indent, indent: as_json(obj, base_indent = base_indent, indent = indent))
    base_indent = getKwarg(kwargs, 'base_indent', 0)
    indent = getKwarg(kwargs, 'indent', 2)

    if l is None:
        return "None"

    if not isinstance(l, list):
        return to_json(l, base_indent = base_indent + indent, indent = indent)

    json_str = "["
    first = True
    for l_item in l:
        if first:
            first = False
        else:
            json_str += ","
        if indent:
            json_str += f"\n{' '*indent}"
        json_str += f"{to_json(l_item, base_indent = base_indent + indent, indent = indent)}"
    if first:                
        json_str += "]"
    else:
        json_str += "\n]"
    return json_str
