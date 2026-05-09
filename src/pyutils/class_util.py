"""Class management utilities"""

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

def create_instance(full_class_path: str, *args, **kwargs):
    cls = get_class(full_class_path)
    return cls(*args, **kwargs)
