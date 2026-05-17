---
sidebar_label: class_util
title: pyutils.class_util
---

Class management utilities

#### load\_class

```python
def load_class(full_class_path: str)
```

Load a class from a full module path string.

**Arguments**:

- `full_class_path` _str_ - The full path to the class in the format &#x27;module.path.ClassName&#x27;.

**Returns**:

- `type` - The loaded class object.

**Raises**:

- `ValueError` - If the full_class_path cannot be split into module and class name.
- `ImportError` - If the module cannot be imported or the class cannot be loaded.
- `AttributeError` - If the class name does not exist in the module.
- `TypeError` - If the loaded object is not a class.

**Example**:

  &gt;&gt;&gt; MyClass = load_class(&#x27;mypackage.mymodule.MyClass&#x27;)

#### get\_class

```python
@cache
def get_class(full_class_path: str)
```

Get a class from a full module path string, caching the result.

**Arguments**:

- `full_class_path` _str_ - The full path to the class in the format &#x27;module.path.ClassName&#x27;.

**Returns**:

- `type` - The loaded class object.

#### create\_instance

```python
def create_instance(spec: str, *args, **kwargs)
```

Create an instance of a class or call a function based on the provided specification string.
The specification can be either:
    - A full class path in the format &#x27;module.path.ClassName&#x27;
    - A function call expression in the format &#x27;module.path.function_name(args, kwargs)&#x27;
Supports:
    create_instance(&quot;mypkg.mod.MyClass&quot;, ...)
    create_instance(&quot;tiktoken.get_encoding(&#x27;gpt2&#x27;)&quot;)

