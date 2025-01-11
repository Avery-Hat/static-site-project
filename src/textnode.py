from enum import Enum


class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        if text_type == TextType.IMAGE:
            self.source_path = text
            self.alt_text = url
        else:
            self.text = text
            self.url = url
        
        self.text_type = text_type

    def __eq__(self, other):
        if self.text_type == TextType.IMAGE:
            return (
                self.text_type == other.text_type
                and self.source_path == other.source_path
                and self.alt_text == other.alt_text
            )
        return (
            self.text_type == other.text_type
            and self.text == other.text
            and self.url == other.url
        )

    def __repr__(self):
        if self.text_type == TextType.IMAGE:
            return f"TextNode(source_path={self.source_path}, {self.text_type.value}, alt_text={self.alt_text})"
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
    
    #PREVIOUS CODE WHICH HAD SRC AND TXT SWAPPED BY ACCIDENT.
# class TextNode:
#     def __init__(self, text, text_type, url=None):
#         self.text = text
#         self.text_type = text_type
#         self.url = url

#     def __eq__(self, other):
#         return (
#             self.text_type == other.text_type
#             and self.text == other.text
#             and self.url == other.url
#         )

#     def __repr__(self):
#         return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
