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
            self.source_path = text       # source_path is the first parameter
            self.alt_text = url          # alt_text comes from url parameter
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


def split_nodes_image(old_nodes):  # This is now a standalone function
    result = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            result.append(node)
            continue
        
        images = extract_markdown_images(node.text)
        if not images:
            result.append(node)
            continue
        
        # Get the first image match
        alt_text, image_url = images[0]
        
        # Split around the image markdown
        image_markdown = f"![{alt_text}]({image_url})"
        sections = node.text.split(image_markdown, 1)
        
        # Add text before image if not empty
        if sections[0]:
            result.append(TextNode(sections[0], TextType.TEXT))
        
        # Add the image node
        result.append(TextNode(image_url, TextType.IMAGE, alt_text))

        # Recursively process any remaining text
        if sections[1]:
            remaining_nodes = split_nodes_image([TextNode(sections[1], TextType.TEXT)])
            result.extend(remaining_nodes)
                
    return result
        
def split_nodes_link(old_nodes):
    result = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            result.append(node)
            continue
        
        links = extract_markdown_links(node.text)
        if not links:
            result.append(node)
            continue
        
        # Get the first link match
        link_text, link_url = links[0]
        
        # Split around the link markdown
        link_markdown = f"[{link_text}]({link_url})"
        sections = node.text.split(link_markdown, 1)
        
        # Add text before link if not empty
        if sections[0]:
            result.append(TextNode(sections[0], TextType.TEXT))
        
        # Add the link node - how should we construct this?
        result.append(TextNode(link_text, TextType.LINK, link_url))

        # Recursively process any remaining text
        if sections[1]:
            remaining_nodes = split_nodes_link([TextNode(sections[1], TextType.TEXT)])
            result.extend(remaining_nodes)
                
    return result