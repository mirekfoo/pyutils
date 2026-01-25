"""
markdown utilities.
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




class GroupMarkdownRenderer:

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
