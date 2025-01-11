
def split_node_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)  # Keeping non-TEXT nodes unchanged
        else:
            first_delimiter = node.text.find(delimiter)
            # If no delimiter found, keep the original node
            if first_delimiter == -1:
                new_nodes.append(node)
            else:
                second_delimiter = node.text.find(delimiter, first_delimiter + len(delimiter))
                if second_delimiter == -1:
                    raise ValueError("Closing delimiter not found")
                else:
                        # Before text (as TextType.TEXT)
                    before_text = node.text[0:first_delimiter]
                    new_nodes.append(TextNode(before_text, TextType.TEXT))
                    
                    # Between delimiters (as the passed in text_type)
                    between_text = node.text[first_delimiter + len(delimiter):second_delimiter]
                    new_nodes.append(TextNode(between_text, text_type))
                    
                    # After text (as TextType.TEXT)
                    after_text = node.text[second_delimiter + len(delimiter):]
                    new_nodes.append(TextNode(after_text, TextType.TEXT))

    
    return new_nodes