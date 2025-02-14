from textnode import TextNode, TextType
from markdown_parser import *
import os
import shutil

def copy_static_directory(src, dst):
    # Cleaning out destination if it exists
    if os.path.exists(dst):
        shutil.rmtree(dst)
    # Making the fresh destination directory
    os.mkdir(dst)

    # Get list of all items in source directory
    for item in os.listdir(src):
        # Create the full paths for source and destination
        src_path = os.path.join(src, item)
        dst_path = os.path.join(dst, item)

        if os.path.isfile(src_path):
            shutil.copy(src_path,dst_path)
        else:
            copy_static_directory(src_path, dst_path)


def main():
    copy_static_directory("static", "public")
    node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(node)

    # Let's add some test cases
    test_images = "Here's ![cute bear](https://bears.com/cute.jpg) and ![cool cat](https://cats.com/cool.jpg)"
    test_links = "Here's [my website](https://mysite.com) and [Boot.dev](https://boot.dev)"
    
    print(extract_markdown_images(test_images))
    print(extract_markdown_links(test_links))

if __name__ == "__main__":
    main()