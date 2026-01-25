"""Type Inspect utilities."""

"""
json_objs_schema(objs)

Optional upgrades (next tier)

If you want to go further:

mark optional fields via "required"

detect fixed-key dictionaries vs maps

unify additionalProperties + properties

emit patternProperties

support unevaluatedProperties (Draft 2020-12)

🏁 Big picture

At this point, your engine supports:

✔ heterogeneous lists

✔ nested flattening

✔ numeric subtype collapse

✔ array lifting

✔ object lifting

That’s basically runtime structural typing → JSON Schema.
"""

import inspect

def inspectObjFunctions(obj):
    """Return the list of functions in the object."""
    l = []
    for name, fn in inspect.getmembers(obj, predicate=callable):
        try:
            sig = inspect.signature(fn)
            l.append(f"{name}{sig}")
        except ValueError:
            l.append(name)
    return l

def inspectObjInstData(obj):
    """Return the list of instance data in the object."""
    l = []
    for name, value in inspect.getmembers(obj):
        if name in getattr(obj, "__dict__", {}):
            #print(f"{name} = {value}")    
            l.append(name)
    return l


def deep_homo_type(obj) -> str:
    """Return the type structure of the object assuming it is homogeneous. At containers return the type of the first element."""

    if isinstance(obj, list):
        return f"list[{deep_type(obj[0])}]" if obj else "list[?]"
    if isinstance(obj, dict):
        k, v = next(iter(obj.items())) if obj else (None, None)
        return f"dict[{deep_type(k)}, {deep_type(v)}]"
    return type(obj).__name__ 


from collections.abc import Iterable

# def deep_type(obj, *, max_items=10):
#     """Return the type structure of the object. 
#        Supports heterogeneous structures.

#     Example output:
    
#     deep_type([1, 2, 3])
#     'list[int]'
    
#     deep_type([1, "2", 3])
#     'list[int | str]'
    
#     deep_type([1, "2", 3, [4, 5]])
#     'list[int | str | list[int]]'

#     deep_type({"a": 1, "b": "2", "c": 3.0, "d": True})
#     'dict[str, int | str | float | bool]'
#     """

#     def tname(o):
#         return type(o).__name__

#     if isinstance(obj, list):
#         if not obj:
#             return "list[?]"

#         types = {deep_type(x) for x in obj[:max_items]}

#         if len(types) == 1:
#             return f"list[{types.pop()}]"
#         else:
#             return f"list[{ ' | '.join(sorted(types)) }]"

#     if isinstance(obj, tuple):
#         return f"tuple[{', '.join(deep_type(x) for x in obj)}]"

#     if isinstance(obj, dict):
#         if not obj:
#             return "dict[?, ?]"

#         ktypes = {deep_type(k) for k in obj.keys()}
#         vtypes = {deep_type(v) for v in obj.values()}

#         k = ktypes.pop() if len(ktypes) == 1 else " | ".join(sorted(ktypes))
#         v = vtypes.pop() if len(vtypes) == 1 else " | ".join(sorted(vtypes))

#         return f"dict[{k}, {v}]"

#     return tname(obj)


# ======== Object-aware deep_type ===============

def deep_type(obj, *, max_items=10, seen=None):
    """Return the type structure of the object. 
       Supports heterogeneous structures.

    Example output:
    
    deep_type([1, 2, 3])
    'list[int]'
    
    deep_type([1, "2", 3])
    'list[int | str]'
    
    deep_type([1, "2", 3, [4, 5]])
    'list[int | str | list[int]]'

    deep_type({"a": 1, "b": "2", "c": 3.0, "d": True})
    'dict[str, int | str | float | bool]'
    """

    if seen is None:
        seen = set()

    oid = id(obj)
    if oid in seen:
        return "(recursive)"
    seen.add(oid)

    # primitives
    if obj is None:
        return "None"
    if isinstance(obj, bool):
        return "bool"
    if isinstance(obj, int):
        return "int"
    if isinstance(obj, float):
        return "float"
    if isinstance(obj, str):
        return "str"

    # list / tuple / set
    if isinstance(obj, (list, tuple, set)):
        inner = {
            deep_type(x, max_items=max_items, seen=seen)
            for x in list(obj)[:max_items]
        }
        return f"[{ ' | '.join(sorted(inner)) }]"

    # dict
    if isinstance(obj, dict):
        key_types = {
            deep_type(k, max_items=max_items, seen=seen)
            for k in obj.keys()
        }
        val_types = {
            deep_type(v, max_items=max_items, seen=seen)
            for v in obj.values()
        }
        return f"dict[{ ' | '.join(key_types) }, { ' | '.join(val_types) }]"

    # user-defined object → GO DEEP
    if hasattr(obj, "__dict__"):
        fields = {
            name: deep_type(val, max_items=max_items, seen=seen)
            for name, val in vars(obj).items()
            if not name.startswith("_")
        }

        inner = ", ".join(f"{k}: {v}" for k, v in fields.items())
        return f"{obj.__class__.__name__}{{{inner}}}"

    # fallback
    return obj.__class__.__name__


from collections.abc import Mapping, Sequence

# def json_schema(obj, *, max_items=10, seen=None):
#     """Return the JSON schema of the object.
#        Recusrion guard.

#         Example output:

#         class Model:
#             def __init__(self):
#                 self.id = 1
#                 self.name = "abc"
#                 self.tags = ["a", "b"]

#         schema = json_schema(Model())

#         Produces:

#         {
#             "type": "object",
#             "title": "Model",
#             "properties": {
#                 "id": { "type": "integer" },
#                 "name": { "type": "string" },
#                 "tags": {
#                 "type": "array",
#                 "items": [{ "type": "string" }]
#                 }
#             }
#         }       

#         TODO:
#         - Add $defs + $ref (true recursion)
#         - Detect heterogenous types
#     """

#     if seen is None:
#         seen = set()

#     t = type(obj)

#     if id(obj) in seen:
#         return {"$ref": "#"}  # recursion guard
#     seen.add(id(obj))

#     # --- primitives ---
#     if obj is None:
#         return {"type": "null"}
#     if isinstance(obj, bool):
#         return {"type": "boolean"}
#     if isinstance(obj, int):
#         return {"type": "integer"}
#     if isinstance(obj, float):
#         return {"type": "number"}
#     if isinstance(obj, str):
#         return {"type": "string"}

#     # --- sequences ---
#     if isinstance(obj, Sequence) and not isinstance(obj, (str, bytes)):
#         items = obj[:max_items]
#         schemas = {repr(type(x)): json_schema(x, max_items=max_items, seen=seen) for x in items}
#         return {
#             "type": "array",
#             "items": list(schemas.values()) if schemas else {}
#         }

#     # --- mappings ---
#     if isinstance(obj, Mapping):
#         props = {}
#         for k, v in list(obj.items())[:max_items]:
#             if isinstance(k, str):
#                 props[k] = json_schema(v, max_items=max_items, seen=seen)
#         return {
#             "type": "object",
#             "properties": props
#         }

#     # --- objects ---
#     props = {}
#     for name, value in inspect.getmembers(obj):
#         if name.startswith("_"):
#             continue
#         if inspect.isroutine(value):
#             continue
#         try:
#             props[name] = json_schema(value, max_items=max_items, seen=seen)
#         except Exception:
#             props[name] = {"type": "unknown"}

#     return {
#         "type": "object",
#         "title": t.__name__,
#         "properties": props
#     }


# =================== + Heterogeneous structures support ======================

# def _merge_schemas(schemas):
#     unique = []
#     seen = set()

#     for s in schemas:
#         key = repr(s)
#         if key not in seen:
#             seen.add(key)
#             unique.append(s)

#     if not unique:
#         return {}

#     if len(unique) == 1:
#         return unique[0]

#     return {"oneOf": unique}


def _normalize_types(schemas):
    types = set()

    for s in schemas:
        t = s.get("type")
        if isinstance(t, str):
            types.add(t)

    # collapse integer → number
    if "number" in types and "integer" in types:
        types.remove("integer")

    if len(types) == 1:
        return {"type": types.pop()}

    return {"oneOf": [{"type": t} for t in sorted(types)]}

# def _merge_schemas(schemas):
#     schemas = [s for s in schemas if s]

#     # extract pure type-only schemas
#     type_only = [s for s in schemas if set(s.keys()) == {"type"}]

#     if len(type_only) == len(schemas):
#         return _normalize_types(type_only)

#     # fallback: full oneOf
#     unique = []
#     seen = set()
#     for s in schemas:
#         key = repr(s)
#         if key not in seen:
#             seen.add(key)
#             unique.append(s)

#     if len(unique) == 1:
#         return unique[0]

#     return {"oneOf": unique}


# ========== array-aware schema merge =========================

def _is_array_schema(s):
    return s.get("type") == "array" and "items" in s

def _merge_array_schemas(schemas):
    item_schemas = [s["items"] for s in schemas]
    return {
        "type": "array",
        "items": _merge_schemas(item_schemas)
    }

# def _merge_schemas(schemas):
#     schemas = [s for s in schemas if s]

#     # 1️⃣ all arrays → lift merge to items
#     if all(_is_array_schema(s) for s in schemas):
#         return _merge_array_schemas(schemas)

#     # 2️⃣ pure type-only schemas → normalize
#     type_only = [s for s in schemas if set(s.keys()) == {"type"}]
#     if len(type_only) == len(schemas):
#         return _normalize_types(type_only)

#     # 3️⃣ fallback → oneOf (deduplicated)
#     unique = []
#     seen = set()
#     for s in schemas:
#         key = repr(s)
#         if key not in seen:
#             seen.add(key)
#             unique.append(s)

#     if len(unique) == 1:
#         return unique[0]

#     return {"oneOf": unique}

# ======== flatten nested oneOf ===============================

def _flatten_oneof(schemas):
    flat = []
    for s in schemas:
        if "oneOf" in s:
            flat.extend(s["oneOf"])
        else:
            flat.append(s)
    return flat

def _merge_schemas(schemas):
    schemas = [s for s in schemas if s]

    # flatten nested oneOfs
    schemas = _flatten_oneof(schemas)

    # all arrays → lift merge to items
    if all(_is_array_schema(s) for s in schemas):
        return {
            "type": "array",
            "items": _merge_schemas([s["items"] for s in schemas])
        }

    # pure type-only schemas → normalize
    type_only = [s for s in schemas if set(s.keys()) == {"type"}]
    if len(type_only) == len(schemas):
        return _normalize_types(type_only)

    # deduplicate
    unique = []
    seen = set()
    for s in schemas:
        key = repr(s)
        if key not in seen:
            seen.add(key)
            unique.append(s)

    if len(unique) == 1:
        return unique[0]

    return {"oneOf": unique}

# ============ flatten nested oneOf =============================

def _is_object_schema(s):
    return s.get("type") == "object"

def _merge_object_schemas(schemas):
    props = {}
    additional = []

    for s in schemas:
        for name, schema in s.get("properties", {}).items():
            props.setdefault(name, []).append(schema)

        if "additionalProperties" in s:
            additional.append(s["additionalProperties"])

    merged = {
        "type": "object",
        "properties": {
            name: _merge_schemas(schemas)
            for name, schemas in props.items()
        }
    }

    if additional:
        merged["additionalProperties"] = _merge_schemas(additional)

    return merged    

def _merge_schemas(schemas):
    schemas = [s for s in schemas if s]

    schemas = _flatten_oneof(schemas)

    # 1️⃣ arrays → lift merge to items
    if all(_is_array_schema(s) for s in schemas):
        return {
            "type": "array",
            "items": _merge_schemas([s["items"] for s in schemas])
        }

    # 2️⃣ objects → merge properties
    if all(_is_object_schema(s) for s in schemas):
        return _merge_object_schemas(schemas)

    # 3️⃣ pure type-only → normalize
    type_only = [s for s in schemas if set(s.keys()) == {"type"}]
    if len(type_only) == len(schemas):
        return _normalize_types(type_only)

    # 4️⃣ fallback → oneOf
    unique = []
    seen = set()
    for s in schemas:
        key = repr(s)
        if key not in seen:
            seen.add(key)
            unique.append(s)

    if len(unique) == 1:
        return unique[0]

    return {"oneOf": unique}

# ===============================================================    

def json_schema(obj, *, max_items=10, seen=None):
    """Return the JSON schema of the object.
       Recusrion guard.

        Example output:

        class Model:
            def __init__(self):
                self.id = 1
                self.name = "abc"
                self.tags = ["a", "b"]

        schema = json_schema(Model())

        Produces:

        {
            "type": "object",
            "title": "Model",
            "properties": {
                "id": { "type": "integer" },
                "name": { "type": "string" },
                "tags": {
                "type": "array",
                "items": [{ "type": "string" }]
                }
            }
        }       

        TODO:
        - Add $defs + $ref (true recursion)
        - Detect heterogenous types
    """

    if seen is None:
        seen = set()

    t = type(obj)

    if id(obj) in seen:
        return {"$ref": "#"}  # recursion guard
    seen.add(id(obj))

    # --- primitives ---
    if obj is None:
        return {"type": "null"}
    if isinstance(obj, bool):
        return {"type": "boolean"}
    if isinstance(obj, int):
        return {"type": "integer"}
    if isinstance(obj, float):
        return {"type": "number"}
    if isinstance(obj, str):
        return {"type": "string"}

    # --- sequences ---
    # Homogeneous → single schema
    # Heterogeneous → oneOf
    elif isinstance(obj, Sequence) and not isinstance(obj, (str, bytes)):
        items = obj[:max_items]

        schemas = [
            json_schema(x, max_items=max_items, seen=seen)
            for x in items
        ]

        return {
            "type": "array",
            "items": _merge_schemas(schemas)
        }

    # --- mappings ---
    elif isinstance(obj, Mapping):
        value_schemas = []

        properties = {}
        for k, v in list(obj.items())[:max_items]:
            if isinstance(k, str):
                s = json_schema(v, max_items=max_items, seen=seen)
                properties[k] = s
                value_schemas.append(s)

        return {
            "type": "object",
            "properties": properties,
            "additionalProperties": _merge_schemas(value_schemas)
        }

    # --- objects ---
    props = {}
    for name, value in inspect.getmembers(obj):
        if name.startswith("_"):
            continue
        if inspect.isroutine(value):
            continue
        try:
            props[name] = json_schema(value, max_items=max_items, seen=seen)
        except Exception:
            props[name] = {"type": "unknown"}

    return {
        "type": "object",
        "title": t.__name__,
        "properties": props
    }


def json_objs_schema(objs, *, max_items=10):
    """
    Detect per-field variance for multiple instances of the same class.

    Return:
        JSON-schema
    """
    
    props = {}

    for obj in objs:
        for name, val in vars(obj).items():
            if name.startswith("_"):
                continue
            props.setdefault(name, []).append(
                json_schema(val, max_items=max_items)
            )

    return {
        name: _merge_schemas(schemas)
        for name, schemas in props.items()
    }

            