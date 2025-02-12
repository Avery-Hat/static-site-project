from textnode import TextNode, TextType
import re

def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches

def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches

def main():
    node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(node)

    # Let's add some test cases
    test_images = "Here's ![cute bear](https://bears.com/cute.jpg) and ![cool cat](https://cats.com/cool.jpg)"
    test_links = "Here's [my website](https://mysite.com) and [Boot.dev](https://boot.dev)"
    
    print(extract_markdown_images(test_images))
    print(extract_markdown_links(test_links))

if __name__ == "__main__":
    main()