"""Class management utilities"""

import ast
import importlib
from functools import cache

def load_class(full_class_path: str):
    try:
        module_path, class_name = full_class_path.rsplit('.', 1)
        module = importlib.import_module(module_path)
        cls = getattr(module, class_name)
        if not isinstance(cls, type):
            raise TypeError(f"{class_name} is not a class")
        return cls
    except (ValueError, ImportError, AttributeError) as e:
        raise ImportError(f"Cannot load class '{full_class_path}': {e}")

@cache
def get_class(full_class_path: str):
    return load_class(full_class_path)

def _call_function(expr: str):
    """
    Handles expressions like:
        tiktoken.get_encoding('gpt2')
    """

    tree = ast.parse(expr, mode="eval")

    if not isinstance(tree.body, ast.Call):
        raise ValueError("Expression is not a function call")

    call_node = tree.body

    # Extract full function path
    func_parts = []

    node = call_node.func

    while isinstance(node, ast.Attribute):
        func_parts.insert(0, node.attr)
        node = node.value

    if isinstance(node, ast.Name):
        func_parts.insert(0, node.id)
    else:
        raise ValueError("Unsupported function path")

    full_func_path = ".".join(func_parts)

    # Split module/function
    module_path, func_name = full_func_path.rsplit(".", 1)

    module = importlib.import_module(module_path)

    func = getattr(module, func_name)

    # Safely evaluate literal args only
    args = [ast.literal_eval(a) for a in call_node.args]

    kwargs = {
        kw.arg: ast.literal_eval(kw.value)
        for kw in call_node.keywords
    }

    return func(*args, **kwargs)


def create_instance(spec: str, *args, **kwargs):
    """
    Supports:
        create_instance("mypkg.mod.MyClass", ...)
        create_instance("tiktoken.get_encoding('gpt2')")
    """

    spec = spec.strip()

    # Function call mode
    if "(" in spec and spec.endswith(")"):
        return _call_function(spec)

    # Class mode
    cls = get_class(spec)

    return cls(*args, **kwargs)
