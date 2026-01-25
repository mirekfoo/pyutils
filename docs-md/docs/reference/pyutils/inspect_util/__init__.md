---
sidebar_label: inspect_util
title: pyutils.inspect_util
---

Type Inspect utilities.

#### inspectObjFunctions

```python
def inspectObjFunctions(obj)
```

Return the list of functions in the object.

#### inspectObjInstData

```python
def inspectObjInstData(obj)
```

Return the list of instance data in the object.

#### deep\_homo\_type

```python
def deep_homo_type(obj) -> str
```

Return the type structure of the object assuming it is homogeneous. At containers return the type of the first element.

#### deep\_type

```python
def deep_type(obj, *, max_items=10, seen=None)
```

Return the type structure of the object.
   Supports heterogeneous structures.

Example output:

deep_type([1, 2, 3])
&#x27;list[int]&#x27;

deep_type([1, &quot;2&quot;, 3])
&#x27;list[int | str]&#x27;

deep_type([1, &quot;2&quot;, 3, [4, 5]])
&#x27;list[int | str | list[int]]&#x27;

deep_type({&quot;a&quot;: 1, &quot;b&quot;: &quot;2&quot;, &quot;c&quot;: 3.0, &quot;d&quot;: True})
&#x27;dict[str, int | str | float | bool]&#x27;

See: examples/deep_type_json_schema.py

#### json\_schema

```python
def json_schema(obj, *, max_items=10, seen=None)
```

Return the JSON schema of the object.
Recusrion guard.

 Example output:

 class Model:
     def __init__(self):
         self.id = 1
         self.name = &quot;abc&quot;
         self.tags = [&quot;a&quot;, &quot;b&quot;]

 schema = json_schema(Model())

 Produces:

 {
     &quot;type&quot;: &quot;object&quot;,
     &quot;title&quot;: &quot;Model&quot;,
     &quot;properties&quot;: {
         &quot;id&quot;: { &quot;type&quot;: &quot;integer&quot; },
         &quot;name&quot;: { &quot;type&quot;: &quot;string&quot; },
         &quot;tags&quot;: {
         &quot;type&quot;: &quot;array&quot;,
         &quot;items&quot;: [{ &quot;type&quot;: &quot;string&quot; }]
         }
     }
 }       

 See: examples/deep_type_json_schema.py

 TODO:
 - Add $defs + $ref (true recursion)

#### json\_objs\_schema

```python
def json_objs_schema(objs, *, max_items=10)
```

Detect per-field variance for multiple instances of the same class.

**Returns**:

  JSON-schema
  
- `See` - examples/deep_type_json_schema.py

