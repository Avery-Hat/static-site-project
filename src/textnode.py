from enum import Enum
from markdown_parser import * #grabbing information for splitnodesimages/links


class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        if text_type == TextType.IMAGE:
            self.url = url            # Store URL for both source_path and url
            self.source_path = url    # Keep source_path for compatibility
            self.alt_text = text      # Alt text should be the main text
        else:
            self.url = url

    def __eq__(self, other):
        return (
            self.text_type == other.text_type
            and self.text == other.text
            and (
                (self.url == other.url if hasattr(self, 'url') else True)
                or
                (self.alt_text == other.alt_text if hasattr(self, 'alt_text') else True)
            )
        )

    def __repr__(self):
        if self.text_type == TextType.IMAGE:
            return f"TextNode(source_path={self.source_path}, {self.text_type.value}, alt_text={self.alt_text})"
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

