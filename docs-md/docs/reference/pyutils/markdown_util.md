---
sidebar_label: markdown_util
title: pyutils.markdown_util
---

Markdown utilities.

## GroupMarkdownRenderer Objects

```python
class GroupMarkdownRenderer()
```

Markdown renderer base class.
Supports rendering of four markdown block types:
- text
- code
- full math
- inline math

## InlineMathMarkdown2HtmlRenderer Objects

```python
class InlineMathMarkdown2HtmlRenderer(GroupMarkdownRenderer)
```

Markdown inline math renderer to HTML.

## InlineMathMarkdownRenderer Objects

```python
class InlineMathMarkdownRenderer(GroupMarkdownRenderer)
```

Markdown inline math renderer to Markdown.

