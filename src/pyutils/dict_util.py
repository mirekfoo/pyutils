"""Dict utilties"""

def dict_merge(d1, d2):
    """Merge two dictionaries, returning a new dictionary with keys from both.

    For each key in the union of d1 and d2, the resulting dictionary will have a value that is a tuple containing:
    - The value from d1 for that key (or None if the key is not in d1)
    - The value from d2 for that key (or None if the key is not in d2)

    Args:
        d1 (dict): First dictionary to merge.
        d2 (dict): Second dictionary to merge.
    Returns:
        dict: A new dictionary where each key is from the union of d1 and d2, and each value is a tuple of (d1_value, d2_value).
    """
    merged = {
        k: (d1.get(k), d2.get(k))
        for k in d1.keys() | d2.keys()
    }
    return merged
