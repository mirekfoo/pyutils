---
sidebar_label: json_util
title: pyutils.json_util
---

JSON formatting utilities.

JSON formatting utilities for converting Python objects to JSON strings with customizable formatting.
This module provides functions to serialize Python objects, dictionaries, and lists to JSON format
with support for:
    - Custom indentation and base indentation levels
    - String truncation for long values
    - Template-based filtering of dictionary properties
    - Regex pattern matching for dynamic property selection
    - Pydantic model serialization

Key Functions:
    - to_json: Convert an object to a JSON string.
    - to_json_pretty: Convert an object to a JSON string with a default indentation of 2 spaces.
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

#### obj2JSON

```python
def obj2JSON(obj)
```

Convert a Python object to a JSON-serializable format.

**Arguments**:

- `obj` - The Python object to be converted.
  

**Returns**:

- `Any` - A JSON-serializable representation of the object, using model_dump()
  if available, otherwise its string representation.

#### as\_json

```python
def as_json(obj, **kwargs) -> str
```

Convert a Python object to a JSON string with customizable indentation.

**Arguments**:

- `obj` - The Python object to be converted to JSON format.
- `**kwargs` - Optional keyword arguments:
  - base_indent (int): The base indentation level (number of spaces) to apply
  to all lines. Default is 0.
  - indent (int): The number of spaces per indentation level. Default is 2.
  

**Returns**:

- `str` - A JSON-formatted string representation of the input object.
  

**Notes**:

  - Uses json.dumps() with a custom obj2JSON serializer for handling non-standard types.
  - If base_indent is greater than 0, all indentation in the output is adjusted
  by adding base_indent spaces to each indented line.

#### patterns\_from\_template

```python
def patterns_from_template(template: Dict) -> Dict
```

Extract regex patterns from a template dictionary.
Filters a template dictionary and returns only the entries where the key
is a compiled regular expression pattern (re.Pattern object).

**Arguments**:

- `template` _Dict_ - A dictionary that may contain re.Pattern objects as keys.
  

**Returns**:

- `Dict` - A new dictionary containing only the key-value pairs where the key
  is a re.Pattern object.
  

**Examples**:

  &gt;&gt;&gt; import re
  &gt;&gt;&gt; template = {
  ...     re.compile(r&#x27;\d+&#x27;): &#x27;number&#x27;,
  ...     &#x27;name&#x27;: &#x27;value&#x27;,
  ...     re.compile(r&#x27;[a-z]+&#x27;): &#x27;letters&#x27;
  ... }
  &gt;&gt;&gt; result = patterns_from_template(template)
  &gt;&gt;&gt; len(result)
  2

#### find\_match\_in\_template

```python
def find_match_in_template(template: Dict,
                           dict_item: str,
                           patterns: Dict = None) -> tuple[bool, Any]
```

Search for a match of dict_item in template or patterns.
First attempts to find an exact match of dict_item as a key in the template dictionary.
If no exact match is found and patterns are provided, performs regex pattern matching
against dict_item using the patterns dictionary keys.

**Arguments**:

- `template` _Dict_ - Dictionary to search for exact key match.
- `dict_item` _str_ - The key/string to search for in template or match against patterns.
- `patterns` _Dict, optional_ - Dictionary where keys are regex patterns to match against dict_item.
  Defaults to None.
  

**Returns**:

- `tuple` - A tuple of (bool, Any) where:
  - bool: True if a match is found (exact or pattern), False otherwise.
  - Any: The value from template or patterns if match is found, None otherwise.
  

**Examples**:

  &gt;&gt;&gt; template = {&quot;key1&quot;: &quot;value1&quot;, &quot;key2&quot;: &quot;value2&quot;}
  &gt;&gt;&gt; find_match_in_template(template, &quot;key1&quot;)
  (True, &quot;value1&quot;)
  &gt;&gt;&gt; patterns = {r&quot;key_regex&quot;: &quot;numeric_value&quot;}
  &gt;&gt;&gt; find_match_in_template(template, &quot;key5&quot;, patterns)
  (True, &quot;numeric_value&quot;)
  &gt;&gt;&gt; find_match_in_template(template, &quot;unknown&quot;)
  (False, None)

#### dict\_as\_json

```python
def dict_as_json(obj: Dict, **kwargs) -> str
```

Convert a dictionary or Pydantic model to a formatted JSON string with optional filtering and truncation.

**Arguments**:

- `obj` _Dict_ - A dictionary or Pydantic model object to convert to JSON string.
- `**kwargs` - Optional keyword arguments:
  - template (dict, optional): A dictionary specifying which properties to include and their string length limits.
  Keys are property names, values are character limits for that property&#x27;s string representation.
  Defaults to None (all properties included).
  - base_indent (int, optional): Base indentation level in spaces. Defaults to 0.
  - indent (int, optional): Indentation step size in spaces. Defaults to 2.
  

**Returns**:

- `str` - A formatted JSON string representation of the object. Properties not included in the template
  are hidden and their count is noted in a comment.
  

**Raises**:

- `TypeError` - If obj is neither a dict nor has a model_dump() method, or if the resulting object is not a dict.
  

**Notes**:

  - Properties matching the template are included with specified string length limits.
  - Non-matching properties are excluded and counted in a comment at the end.
  - The output uses indentation for readability when indent &gt; 0.
  - If no properties match the template, only &quot;{}&quot; is returned.

#### list\_as\_json

```python
def list_as_json(l: List, **kwargs) -> str
```

Convert a list to a formatted JSON string representation.

**Arguments**:

- `l` _List_ - The list to convert to JSON format. Can be None or a non-list object.
- `**kwargs` - Optional keyword arguments:
  - to_json (callable): Custom function to convert objects to JSON strings.
- `Default` - as_json with specified indentation.
- `Signature` - to_json(obj, base_indent, indent) -&gt; str
  - base_indent (int): Base indentation level in spaces. Default: 0
  - indent (int): Indentation increment in spaces. Default: 2
  

**Returns**:

- `str` - A formatted JSON string representation of the input.
  - Returns &quot;None&quot; if input is None.
  - If input is not a list, returns the JSON representation of that object.
  - If input is a list, returns a bracketed JSON array with proper formatting
  and indentation.
  

**Examples**:

  &gt;&gt;&gt; list_as_json([1, 2, 3])
  &#x27;[\n  1,\n  2,\n  3\n]&#x27;
  &gt;&gt;&gt; list_as_json(None)
  &#x27;None&#x27;
  &gt;&gt;&gt; list_as_json(42)
  &#x27;42&#x27;

#### to\_json

```python
def to_json(obj, indent=None) -> str
```

Convert an object to a JSON string.

**Arguments**:

- `obj` - The object to convert to JSON.
- `indent` _int, optional_ - If ``indent`` is a non-negative integer, then JSON array elements and
  object members will be pretty-printed with that indent level. An indent
  level of 0 will only insert newlines. ``None`` is the most compact
  representation.
  

**Returns**:

- `str` - The JSON string representation of the object.

#### to\_json\_pretty

```python
def to_json_pretty(obj) -> str
```

Convert an object to a JSON string with a default indentation of 2 spaces.

**Arguments**:

- `obj` - The object to convert to JSON.
  

**Returns**:

- `str` - The JSON string representation of the object with a default indentation of 2 spaces.

