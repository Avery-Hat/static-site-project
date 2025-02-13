#chapter 4, lesson 3: converting full md doc into a single ParentNode.
from markdown_parser import *
from htmlnode import *
from text_to_nodes import *
from textnode import *
from text_to_html import *

def markdown_to_html_node(markdown):
    parent_node = ParentNode('div', [])
    blocks = markdown_to_blocks(markdown)
    
    for block in blocks:
        block_type = block_to_block_type(block)

        if block_type == 'heading' or block_type == 'mixed_heading_paragraph':
            lines = block.split('\n')

            for line in lines:
                if line.startswith('#'):
                    count = 0
                    for char in line:
                        if char == '#':
                            count += 1
                        else:
                            break
                    if len(line) > count and line[count] == ' ':
                        text = line[count:].strip()
                        children = text_to_children(text)
                        heading_node = ParentNode(f'h{count}', children)
                        parent_node.children.append(heading_node)
                else:
                    # Process remaining lines as paragraph if it's a mixed block
                    paragraph_text = line.strip()
                    if paragraph_text:
                        children = text_to_children(paragraph_text)
                        paragraph_node = ParentNode('p', children)
                        parent_node.children.append(paragraph_node)

        elif block_type == 'quote':
            lines = block.split('\n')
            # Remove both '>' and the space after it if present
            text = '\n'.join(line.lstrip('> ').strip() for line in lines)
            children = text_to_children(text)
            quote_node = ParentNode('blockquote', children)
            parent_node.children.append(quote_node)

        elif block_type == 'paragraph':
            children = text_to_children(block)
            paragraph_node = ParentNode('p', children)
            parent_node.children.append(paragraph_node)

        elif block_type == 'code':
            # Split into lines and remove the first and last lines (which contain ```)
            lines = block.split('\n')
            if len(lines) >= 2:  # Make sure we have at least opening and closing ```
                # Join all lines except first and last, preserving internal newlines
                code_content = '\n'.join(lines[1:-1])
                code_node = LeafNode('code', code_content)
                pre_node = ParentNode('pre', [code_node])
                parent_node.children.append(pre_node)

        elif block_type == 'unordered_list':
            ul_node = ParentNode('ul', [])
            lines = block.split('\n')
            for line in lines:
                # Remove either '* ' or '- ' from start
                if line.startswith('* '):
                    text = line[2:].strip()
                elif line.startswith('- '):
                    text = line[2:].strip()
                children = text_to_children(text)
                li_node = ParentNode('li', children)
                ul_node.children.append(li_node)
            parent_node.children.append(ul_node)
        
        elif block_type == 'ordered_list':
            ol_node = ParentNode('ol', [])
            lines = block.split('\n')
            for line in lines:
                period_index = line.index('.')
                text = line[period_index + 2:]
                children = text_to_children(text)
                li_node = ParentNode('li', children)
                ol_node.children.append(li_node)
            parent_node.children.append(ol_node)

    return parent_node


def text_to_children(text):
    # First convert text to TextNodes
    text_nodes = text_to_textnodes(text)
    # Then convert TextNodes to HTMLNodes
    return [text_node_to_html_node(node) for node in text_nodes]  