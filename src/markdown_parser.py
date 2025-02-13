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
    final_blocks = []

    for block in blocks:
        lines = block.strip().split('\n')
        current_block = []
        current_type = None

        for line in lines:
            line_type = None
            if line.startswith('> '):
                line_type = 'quote'
            elif line.startswith('#'):
                line_type = 'heading'
            elif line.startswith('* ') or line.startswith('- '):
                line_type = 'list'
            elif line.strip().startswith('```'):
                line_type = 'code'
            # Add more line type checks as needed

            if current_type and line_type and current_type != line_type:
                # If type changes, start a new block
                if current_block:
                    final_blocks.append('\n'.join(current_block))
                current_block = [line]
                current_type = line_type
            else:
                current_block.append(line)
                if not current_type:
                    current_type = line_type

        if current_block:
            final_blocks.append('\n'.join(current_block))

    return [block for block in final_blocks if block.strip()]

#chapter 4, part 2: checking blocks of md text and returning string representing
# the types of block it is (paragraph,heading,code,quote,unordered_list,ordered_list)
def block_to_block_type(block):
    lines = block.split('\n')
    
    # Code blocks (check first since they use special markers)
    if len(lines) >= 2:
        first_line = lines[0].strip()
        last_line = lines[-1].strip()
        if first_line == '```' and last_line == '```':
            return 'code'
    
    # Heading (check early since it's a single-line pattern)
    if block.startswith('#'):
        hash_count = 0
        for char in block:
            if char == '#':
                hash_count += 1
            else:
                break
        if hash_count <= 6 and len(block) > hash_count and block[hash_count] == ' ':
            return 'heading'
    
    # Block quotes
    all_quotes = True
    for line in lines:
        if not (line.startswith("> ") or line.startswith(">")):
            all_quotes = False
    if all_quotes:
        return 'quote'
        
    # Unordered lists
    all_unordered = True
    for line in lines:
        if not (line.startswith('* ') or line.startswith('- ')):
            all_unordered = False
    if all_unordered:
        return 'unordered_list'
    
    # Ordered lists
    all_ordered = True
    for i, line in enumerate(lines, start=1):
        if not line.startswith(f"{i}. "):
            all_ordered = False
    if all_ordered:
        return 'ordered_list'
    
    # Paragraph (default case)
    return 'paragraph'