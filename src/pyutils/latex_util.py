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

    for key, val in latex_math_operands_to_unicode_replacements.items():
        latex = latex.replace(key, val)

    return latex

def latex_math_operands_to_html(latex):

    for key, val in latex_math_operands_to_html_replacements.items():
        latex = latex.replace(key, val)

    return latex

def latex_subscripts_to_text(latex):
    latex = re.sub(r"_([A-Za-z0-9]+)", r"(\1)", latex) # short subscript
    latex = re.sub(r"_\{([A-Za-z0-9]+)\}", r"(\1)", latex) # long subscript
    return latex

def latex_subscripts_to_html(latex):
    latex = re.sub(r"_([A-Za-z0-9]+)", r"<sub>\1</sub>", latex) # short subscript
    latex = re.sub(r"_\{([A-Za-z0-9]+)\}", r"<sub>\1</sub>", latex) # long subscript
    return latex

def latex_boxed_to_md(latex):
    latex = re.sub(r"\\boxed\{(.*?)\}", r"**\1**", latex)
    return latex

def latex_boxed_to_html(latex):
    latex = re.sub(r"\\boxed\{(.*?)\}", r'<span class="boxed">\1</span>', latex)
    return latex

