"""String utility functions."""

# # def truncated_string(s: str, original_length: int) -> str:
#     """Mark a string as truncated, indicating how many characters were truncated"""
    
#     truncated_s = f"[{original_length} chars]{s}"
#     if len(s) < original_length:
#         truncated_s += f"...[more {original_length - len(s)} chars]"
#     #     return f"[{original_length} chars]{s}...[more {original_length - len(s)} chars]"
#     # else:
#     #     return s
#     return truncated_s

def truncate_string(s: str, max_length: int = 100) -> str:
    """
    Truncate a string to a maximum length, adding '...[more n chars]' if truncated..

    Args:
        s (str): The string to truncate.
        max_length (int): The maximum length of the string before truncation.

    Returns:
        str: The truncated string.
    """

    s_len = len(s)
    truncated_s = s[:max_length]
    truncated_s_len = len(truncated_s)
    truncated_s = f"[{s_len} chars]{truncated_s}"
    if truncated_s_len < s_len:
        truncated_s += f"...[more {s_len - truncated_s_len} chars]"
    return truncated_s

    #return truncated_string(s[:max_length], len(s))
