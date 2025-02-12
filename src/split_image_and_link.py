from textnode import TextNode, TextType
from markdown_parser import extract_markdown_images, extract_markdown_links

def split_nodes_image(old_nodes):
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
        result.append(TextNode(alt_text, TextType.IMAGE, image_url))

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
        

        result.append(TextNode(link_text, TextType.LINK, link_url))

        # Recursively process any remaining text
        if sections[1]:
            remaining_nodes = split_nodes_link([TextNode(sections[1], TextType.TEXT)])
            result.extend(remaining_nodes)
                
    return result
