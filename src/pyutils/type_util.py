"""Type utilities."""

def indexable(obj):
    """Return True if the object is indexable."""
    try:
        obj[0]
    except KeyError:
        supports_indexing = True
    except TypeError:
        supports_indexing = False
    except Exception:
        supports_indexing = False
    else:
        supports_indexing = True
    return supports_indexing