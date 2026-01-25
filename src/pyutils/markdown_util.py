"""
Markdown utilities.
"""

import re

MD_BLOCK_RE = re.compile(
    r"""
    (?P<code>```(\w+)?\n.*?\n```)|        # fenced code
    (?P<full_math>\$\$.*?\$\$)|           # display math
    (?P<inline_math>\$[^$\n]+\$)          # inline math
    """,
    re.DOTALL | re.VERBOSE
)

# ------------------------------------------------------------

class GroupMarkdownRenderer:

    """
    Markdown renderer base class.
    Supports rendering of four markdown block types:
    - text
    - code
    - full math
    - inline math
    """

    def __init__(self, renders_map, data, filters=[]):
        self.renders_map = renders_map
        self.data = data
        self.filters = filters

    def render_markdown(self, md):
        pos = 0
        for m in MD_BLOCK_RE.finditer(md):
            if m.start() > pos:
                self.renders_map["text"](md[pos:m.start()], self.data)

            if m.group("code"):
                self.renders_map["code"](m.group("code"), self.data)

            elif m.group("full_math"):
                self.renders_map["full_math"](m.group("full_math")[2:-2], self.data)

            elif m.group("inline_math"):
                self.renders_map["inline_math"](m.group("inline_math")[1:-1], self.data)

            pos = m.end()

        if pos < len(md):
            self.renders_map["text"](md[pos:], self.data)

    def _apply_filters(self, md):
        for filter in self.filters:
            md = filter(md)
        return md

# ------------------------------------------------------------

from pyutils.latex_util import latex_math_operands_to_html, latex_subscripts_to_html, latex_boxed_to_html

class InlineMathMarkdown2HtmlRenderer(GroupMarkdownRenderer):

    """
    Markdown inline math renderer to HTML.
    """

    # TODO use MathJax or KaTeX for render latex (math) to html

    filters = [ latex_math_operands_to_html, latex_subscripts_to_html, latex_boxed_to_html ]

    def __init__(self, renders_map, data):
        super().__init__(renders_map, self, InlineMathMarkdown2HtmlRenderer.filters)
        self.html = ""
        self.paragraph = ""

    def _close_paragraph(self):
        if self.paragraph:
            self.html += "<p>" + self.paragraph + "</p>"
            self.paragraph = ""

    def _add_paragraph(self, html):
        self._close_paragraph()
        self.html += html

    def _add_to_paragraph(self, html):
        self.paragraph += html

    def __call__(self, md):
        self.html = ""
        self.paragraph = ""
        super().render_markdown(md)
        self._close_paragraph()
        return self.html

# ------------------------------------------------------------

from pyutils.latex_util import latex_math_operands_to_unicode, latex_subscripts_to_html, latex_boxed_to_md

class InlineMathMarkdownRenderer(GroupMarkdownRenderer):

    """
    Markdown inline math renderer to Markdown.
    """

    # NOTE Gradio Markdown renderer ignores CSS styles
    
    #filters = [ latex_math_operands_to_unicode, latex_subscripts_to_html, latex_boxed_to_html ]
    filters = [ latex_math_operands_to_unicode, latex_subscripts_to_html, latex_boxed_to_md ]

    def _add_rendered_markdown(self, md):
        self.rendered_markdown += md

    renders_map = {
        "text": lambda md, data: data._add_rendered_markdown(md),
        "code": lambda md, data: data._add_rendered_markdown(md),
        "full_math": lambda latex, data: data._add_rendered_markdown(f"$${latex}$$"),
        "inline_math": lambda latex, data: data._add_rendered_markdown(f"_{data._apply_filters(latex)}_"),
    }

    # BOX_FRAME_COLOR = "#000000"

    # def getCSS():
    #     return f"""
    #         .boxed {{
    #             border: 1px solid {InlineMathMarkdownRenderer.BOX_FRAME_COLOR};
    #             padding: 0.2em 0.5em;
    #             margin: 0 0.1em;
    #             display: inline-block;
    #         }}
    #         """

    # def getHTMLStyling():
    #     return f"<style>{InlineMathMarkdownRenderer.getCSS()}</style>"

    def __init__(self):
        super().__init__(InlineMathMarkdownRenderer.renders_map, self, InlineMathMarkdownRenderer.filters)
        self.rendered_markdown = ""

    def __call__(self, md):
        self.rendered_markdown = ""
        super().render_markdown(md)
        #return InlineMathMarkdownRenderer.getHTMLStyling() + self.rendered_markdown
        return self.rendered_markdown
