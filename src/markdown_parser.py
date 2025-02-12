#created away from main to stop recursive actions (accessing textnode to access main;)
# main was accessing textnode.
import re

def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches

def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches

def markdown_to_blocks(markdown):
    blocks = markdown.split('\n\n')
    cleaned_blocks = []

    for block in blocks:
        cleaned_block = block.strip()
        
        if cleaned_block != "":
            cleaned_blocks.append(cleaned_block)
    return cleaned_blocks