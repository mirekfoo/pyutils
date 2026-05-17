---
sidebar_label: latex_util
title: pyutils.latex_util
---

latex utilities.

#### latex\_math\_operands\_to\_unicode

```python
def latex_math_operands_to_unicode(latex)
```

Convert LaTeX math operand commands to Unicode symbols.

**Arguments**:

- `latex` _str_ - A string containing LaTeX math expressions.
  

**Returns**:

- `str` - The converted string where recognized LaTeX operand commands
  such as &quot;\le&quot;, &quot;\ge&quot;, and &quot;\times&quot; are replaced with
  their Unicode equivalents.
  

**Notes**:

  This function uses a fixed replacement mapping defined in
  `latex_math_operands_to_unicode_replacements`. Only keys present in
  that mapping are replaced; other LaTeX syntax is left unchanged.

#### latex\_math\_operands\_to\_html

```python
def latex_math_operands_to_html(latex)
```

Convert LaTeX math operand commands to HTML numeric character references.

**Arguments**:

- `latex` _str_ - A string containing LaTeX math expressions.
  

**Returns**:

- `str` - The converted string where recognized LaTeX operand commands
  such as &quot;\le&quot;, &quot;\ge&quot;, and &quot;\times&quot; are replaced with
  their HTML numeric character reference equivalents (e.g., &quot;&amp;`x2264`;&quot;).
  

**Notes**:

  This function uses a replacement mapping defined in
  `latex_math_operands_to_html_replacements`, which is dynamically
  generated from `latex_math_operands_to_unicode_replacements`.
  Only keys present in that mapping are replaced; other LaTeX syntax
  is left unchanged.

#### latex\_subscripts\_to\_text

```python
def latex_subscripts_to_text(latex)
```

Convert LaTeX subscripts to plain text notation.

**Arguments**:

- `latex` _str_ - A string containing LaTeX expressions with subscript
  syntax, such as `_i` or `_{ij}`.
  

**Returns**:

- `str` - The processed string where LaTeX subscripts are replaced with
  parenthesized text, for example `_i` becomes `(i)` and
  `_{ij}` becomes `(ij)`.
  

**Notes**:

  Only alphanumeric subscript identifiers are handled. Other LaTeX
  syntax is left unchanged.

#### latex\_subscripts\_to\_html

```python
def latex_subscripts_to_html(latex)
```

Convert LaTeX subscript syntax to HTML &lt;sub&gt; tags.

This function replaces short subscript forms like `_i` and braced
forms like `_{ij}` with HTML `<sub>...</sub>` equivalents. Only
alphanumeric subscript identifiers are handled; other LaTeX syntax
is left unchanged.

**Arguments**:

- `latex` _str_ - A string containing LaTeX expressions that may
  include subscript syntax (`_x` or `_{xy}`).
  

**Returns**:

- `str` - The input string with LaTeX subscripts converted to HTML
  `<sub>` tags. For example, `a_i` -&gt; `a<sub>i</sub>` and
  `_{ij}`0 -&gt; `_{ij}`1.
  

**Notes**:

  - The function performs two regex substitutions:
  1) short form `_x` -&gt; `_{ij}`3
  2) braced form `_{xy}` -&gt; `_{ij}`5
  - Only letters and digits are accepted inside the subscript
  (pattern `_{ij}`6).

#### latex\_boxed\_to\_md

```python
def latex_boxed_to_md(latex)
```

Convert LaTeX oxed{...} constructs to Markdown bold text.

This function finds occurrences of the LaTeX command ``oxed{...}``
and replaces them with Markdown bold syntax ``**...**``. It uses a
non-greedy regular expression so that nested or multiple boxed
constructs on the same line are handled individually.

**Arguments**:

- `latex` _str_ - Input string that may contain LaTeX ``oxed{...}``
  constructs.
  

**Returns**:

- `str` - A new string where each ``oxed{...}`` has been replaced by
  the equivalent Markdown bold text ``**...**``.
  

**Notes**:

  - Only the simple form ``oxed{...}`` is supported; contents
  inside the braces are captured by ``(.*?)`` and inserted
  verbatim into the Markdown output.
  - This function does not perform any escaping of Markdown
  characters that may appear inside the boxed content.

#### latex\_boxed\_to\_html

```python
def latex_boxed_to_html(latex)
```

Convert LaTeX oxed{...} constructs to HTML span elements.

This function finds occurrences of the LaTeX command ``oxed{...}``
and replaces them with HTML ``&lt;span class=&quot;boxed&quot;&gt;...&lt;/span&gt;`` elements.
It uses a non-greedy regular expression so that nested or multiple boxed
constructs on the same line are handled individually.

**Arguments**:

- `latex` _str_ - Input string that may contain LaTeX ``oxed{...}``
  constructs.
  

**Returns**:

- `str` - A new string where each ``oxed{...}`` has been replaced by
  the equivalent HTML span element ``&lt;span class=&quot;boxed&quot;&gt;...&lt;/span&gt;``.
  

**Notes**:

  - Only the simple form ``oxed{...}`` is supported; contents
  inside the braces are captured by ``(.*?)`` and inserted
  verbatim into the HTML output.
  - This function does not perform any escaping of HTML characters
  that may appear inside the boxed content. Callers should handle
  HTML escaping if necessary.

