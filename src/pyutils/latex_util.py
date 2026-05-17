"""
latex utilities.
"""

import re

latex_math_operands_to_unicode_replacements = {
        r"\le": "≤",
        r"\ge": "≥",
        r"\times": "×",
        r"\pm": "±",
        r"\neq": "≠",
        r"\approx": "≈",
        r"\infty": "∞",
        r"\cdot": "·",
        r"\ldots": "…",
        # Add more as needed
    }

latex_math_operands_to_html_replacements = {
    key: f"&#x{ord(val):x};" for key, val in latex_math_operands_to_unicode_replacements.items()
}

def latex_math_operands_to_unicode(latex):
    """Convert LaTeX math operand commands to Unicode symbols.

    Args:
        latex (str): A string containing LaTeX math expressions.

    Returns:
        str: The converted string where recognized LaTeX operand commands
            such as "\\le", "\\ge", and "\\times" are replaced with
            their Unicode equivalents.

    Notes:
        This function uses a fixed replacement mapping defined in
        `latex_math_operands_to_unicode_replacements`. Only keys present in
        that mapping are replaced; other LaTeX syntax is left unchanged.
    """

    for key, val in latex_math_operands_to_unicode_replacements.items():
        latex = latex.replace(key, val)

    return latex

def latex_math_operands_to_html(latex):
    """Convert LaTeX math operand commands to HTML numeric character references.

    Args:
        latex (str): A string containing LaTeX math expressions.

    Returns:
        str: The converted string where recognized LaTeX operand commands
            such as "\\le", "\\ge", and "\\times" are replaced with
            their HTML numeric character reference equivalents (e.g., "&#x2264;").

    Notes:
        This function uses a replacement mapping defined in
        `latex_math_operands_to_html_replacements`, which is dynamically
        generated from `latex_math_operands_to_unicode_replacements`.
        Only keys present in that mapping are replaced; other LaTeX syntax
        is left unchanged.
    """
    for key, val in latex_math_operands_to_html_replacements.items():
        latex = latex.replace(key, val)

    return latex

def latex_subscripts_to_text(latex):
    """Convert LaTeX subscripts to plain text notation.

    Args:
        latex (str): A string containing LaTeX expressions with subscript
            syntax, such as `_i` or `_{ij}`.

    Returns:
        str: The processed string where LaTeX subscripts are replaced with
            parenthesized text, for example `_i` becomes `(i)` and
            `_{ij}` becomes `(ij)`.

    Notes:
        Only alphanumeric subscript identifiers are handled. Other LaTeX
        syntax is left unchanged.
    """

    # Convert short subscript forms like `_i` to `(i)`.
    latex = re.sub(r"_([A-Za-z0-9]+)", r"(\1)", latex)
    # Convert long (braced) subscript forms like `_{ij}` to `(ij)`.
    latex = re.sub(r"_\{([A-Za-z0-9]+)\}", r"(\1)", latex)
    return latex

def latex_subscripts_to_html(latex):
    """Convert LaTeX subscript syntax to HTML <sub> tags.

    This function replaces short subscript forms like `_i` and braced
    forms like `_{ij}` with HTML `<sub>...</sub>` equivalents. Only
    alphanumeric subscript identifiers are handled; other LaTeX syntax
    is left unchanged.

    Args:
        latex (str): A string containing LaTeX expressions that may
            include subscript syntax (`_x` or `_{xy}`).

    Returns:
        str: The input string with LaTeX subscripts converted to HTML
            `<sub>` tags. For example, `a_i` -> `a<sub>i</sub>` and
            `b_{ij}` -> `b<sub>ij</sub>`.

    Notes:
        - The function performs two regex substitutions:
            1) short form `_x` -> `<sub>x</sub>`
            2) braced form `_{xy}` -> `<sub>xy</sub>`
        - Only letters and digits are accepted inside the subscript
          (pattern `[A-Za-z0-9]+`).
    """

    # Replace short subscript forms like `_i` with `<sub>i</sub>`.
    latex = re.sub(r"_([A-Za-z0-9]+)", r"<sub>\1</sub>", latex)
    # Replace long (braced) subscript forms like `_{ij}` with `<sub>ij</sub>`.
    latex = re.sub(r"_\{([A-Za-z0-9]+)\}", r"<sub>\1</sub>", latex)
    return latex

def latex_boxed_to_md(latex):
    """Convert LaTeX \boxed{...} constructs to Markdown bold text.

    This function finds occurrences of the LaTeX command ``\boxed{...}``
    and replaces them with Markdown bold syntax ``**...**``. It uses a
    non-greedy regular expression so that nested or multiple boxed
    constructs on the same line are handled individually.

    Args:
        latex (str): Input string that may contain LaTeX ``\boxed{...}``
            constructs.

    Returns:
        str: A new string where each ``\boxed{...}`` has been replaced by
            the equivalent Markdown bold text ``**...**``.

    Notes:
        - Only the simple form ``\boxed{...}`` is supported; contents
          inside the braces are captured by ``(.*?)`` and inserted
          verbatim into the Markdown output.
        - This function does not perform any escaping of Markdown
          characters that may appear inside the boxed content.
    """

    latex = re.sub(r"\\boxed\{(.*?)\}", r"**\1**", latex)
    return latex

def latex_boxed_to_html(latex):
    """Convert LaTeX \boxed{...} constructs to HTML span elements.

    This function finds occurrences of the LaTeX command ``\boxed{...}``
    and replaces them with HTML ``<span class="boxed">...</span>`` elements.
    It uses a non-greedy regular expression so that nested or multiple boxed
    constructs on the same line are handled individually.

    Args:
        latex (str): Input string that may contain LaTeX ``\boxed{...}``
            constructs.

    Returns:
        str: A new string where each ``\boxed{...}`` has been replaced by
            the equivalent HTML span element ``<span class="boxed">...</span>``.

    Notes:
        - Only the simple form ``\boxed{...}`` is supported; contents
          inside the braces are captured by ``(.*?)`` and inserted
          verbatim into the HTML output.
        - This function does not perform any escaping of HTML characters
          that may appear inside the boxed content. Callers should handle
          HTML escaping if necessary.
    """
    latex = re.sub(r"\\boxed\{(.*?)\}", r'<span class="boxed">\1</span>', latex)
    return latex

