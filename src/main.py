from textnode import TextNode, TextType
from markdown_parser import *
import os
import shutil
from block_to_HTML import markdown_to_html_node
from title_extractor import * #importing title extractor

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
    # copying directory first
    copy_static_directory("static", "public")
    
    #generate main page, index.html
    generate_pages_recursive(
    dir_path_content="content",  # Process all markdown files in the content directory
    template_path="template.html",  # Path to the HTML template
    dest_dir_path="public"  # Output all processed files into the public directory
)


def generate_page(from_path, template_path, dest_path):
    # Print status
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    # Read the markdown file
    with open(from_path, "r") as f:
        markdown_content = f.read()

    # Read the template file
    with open(template_path, "r") as f:
        template_content = f.read()

    # Convert markdown to HTML
    html_content = markdown_to_html_node(markdown_content).to_html()

    # Extract the title
    title = extract_title(markdown_content)

    # Replace placeholders
    full_html = template_content.replace("{{ Title }}", title).replace("{{ Content }}", html_content)
    # Ensure the destination directory exists
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    # Write the final HTML to the destination file
    with open(dest_path, "w") as f:
        f.write(full_html)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    os.makedirs(dest_dir_path, exist_ok=True)
    entries = os.listdir(dir_path_content)
    for entry in entries:
        source_path = os.path.join(dir_path_content, entry)
        dest_path = os.path.join(dest_dir_path, entry)
        
        if os.path.isfile(source_path):
            if source_path.endswith(".md"):
                dest_path = dest_path[:-3] + ".html"
                generate_page(source_path, template_path, dest_path)
        elif os.path.isdir(source_path):  # Ensure we're dealing with a directory
            generate_pages_recursive(source_path, template_path, dest_path)

if __name__ == "__main__":
    main()