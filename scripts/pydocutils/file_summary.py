import re
from enum import Enum

class HeaderParseState(Enum):
    BEFORE_HEADER = 1
    IN_HEADER = 2
    AFTER_HEADER = 3

def get_first_doc_sentence(filepath):
    content_before_chapter = []
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            header_parse_state = HeaderParseState.BEFORE_HEADER
            for line in f:
                stripped = line.strip()
                # Check for header parsing
                if stripped == "---":
                    if header_parse_state == HeaderParseState.BEFORE_HEADER:
                        header_parse_state = HeaderParseState.IN_HEADER
                        continue
                    elif header_parse_state == HeaderParseState.IN_HEADER:
                        header_parse_state = HeaderParseState.AFTER_HEADER
                        continue
                elif header_parse_state == HeaderParseState.IN_HEADER:
                    continue
                # Check for chapter marker (header)
                if stripped.startswith('#'):
                    break
                content_before_chapter.append(line)
    except FileNotFoundError:
        return "Error: File not found."

    # Join lines and strip leading/trailing whitespace
    text = "".join(content_before_chapter).strip()
    
    if not text:
        return ""

    # Normalize whitespace (replace newlines with spaces)
    text = " ".join(text.split())

    # Regex to find the first sentence.
    # It looks for non-greedy characters until a punctuation mark (. ! ?)
    # followed by a whitespace or end of string.
    # Note: This is a basic implementation and might fail on abbreviations like "Mr.".
    match = re.search(r'(.*?[.!?])(\s|$)', text)
    if match:
        return match.group(1)
    else:
        # If no sentence delimiter is found, return the text as is.
        return text
