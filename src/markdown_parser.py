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

#chapter 4, part 2: checking blocks of md text and returning string representing
# the types of block it is (paragraph,heading,code,quote,unordered_list,ordered_list)
def block_to_block_type(block):
    #heading
    if block.startswith('#'):
        hash_count = 0
        for char in block:
            if char == '#':
                hash_count += 1
            else:
                break
        if hash_count <= 6 and len(block) > hash_count and block[hash_count] == ' ':
            return 'heading'
        
    #unordered_lists
    lines = block.split('\n') #reusing variable for ordered_lists
    all_unordered = True
    #checking each line
    for line in lines:
        if not (line.startswith('* ') or line.startswith('- ')):
            all_unordered = False
    if all_unordered:
        return 'unordered_list'
    
    #ordered_lists
    all_ordered = True
    for i, line in enumerate(lines, start=1):
        if not line.startswith(f"{i}. "):
            all_ordered = False
    if all_ordered:
        return 'ordered_list'
    
    #code
    if len(lines) >= 2:  # make sure we have at least 2 lines
        first_line = lines[0].strip()
        last_line = lines[-1].strip()
        if first_line == ('```') and last_line == '```':
            return 'code'

    #block_quotes
    all_quotes = True
    for line in lines:
        if not (line.startswith("> ") or line.startswith(">")):
            all_quotes = False
    if all_quotes:
        return 'quote'
    
    return 'paragraph'