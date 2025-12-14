"""JSON formatting utilities"""

from typing import Any, Dict, List, Optional
import json
import re

from utils.str_util import truncate_string
from utils.kwargs import getKwarg

def obj2JSON(obj):
    """Helper function to convert objects to JSON-serializable format."""
    try:
        return obj.model_dump()
    except Exception:
        return str(obj)

#def as_json(obj, indent=2) -> str:
def as_json(obj, **kwargs) -> str:
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
    patterns = {}
    for key in template:
        if isinstance(key, re.Pattern):
            patterns[key] = template[key]

    return patterns 

def find_match_in_template(template: Dict, dict_item: str, patterns: Dict = None) -> (bool, Any):
    if dict_item in template:
        return (True, template[dict_item])

    if patterns:
        for pattern in patterns:
            if re.fullmatch(pattern, dict_item):
                return (True, patterns[pattern])

    return (False, None)

# pattern = re.compile(r"\d+")

#def dict_as_json(obj: Dict, template: Dict = None, indent: int = 2) -> str:
def dict_as_json(obj: Dict, **kwargs) -> str:
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

#def list_as_json(list: List, indent: int = 2, to_json = lambda obj, indent: as_json(obj, indent)) -> str:
def list_as_json(l: List, **kwargs) -> str:
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
