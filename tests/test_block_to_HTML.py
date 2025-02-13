#located in block_to_HTML.py, chapter 4, part 3
import unittest
from block_to_HTML import *

class TestBlockToHTML(unittest.TestCase):
    def test_paragraph(self):
        node = markdown_to_html_node("This is a paragraph")
        self.assertEqual(
            node.to_html(),
            "<div><p>This is a paragraph</p></div>"
        )
    
    def test_heading(self):
        node = markdown_to_html_node("# Heading")
        self.assertEqual(
            node.to_html(),
            "<div><h1>Heading</h1></div>"
        )
    
    def test_blockquote(self):
        node = markdown_to_html_node("> This is a quote")
        self.assertEqual(
            node.to_html(),
            "<div><blockquote>This is a quote</blockquote></div>"
        )
    
    def test_code_block(self):
        node = markdown_to_html_node("```\ncode block\n```")
        self.assertEqual(
            node.to_html(),
            "<div><pre><code>code block</code></pre></div>"
        )

    def test_multiple_blocks(self):
        markdown = """# Header
This is a paragraph.
> This is a quote."""
        node = markdown_to_html_node(markdown)
        self.assertEqual(
            node.to_html(),
            "<div><h1>Header</h1><p>This is a paragraph.</p><blockquote>This is a quote.</blockquote></div>"
        )

    def test_lists(self):
        markdown = """* Item 1
* Item 2
* Item 3"""
        node = markdown_to_html_node(markdown)
        self.assertEqual(
            node.to_html(),
            "<div><ul><li>Item 1</li><li>Item 2</li><li>Item 3</li></ul></div>"
        )

    def test_inline_formatting(self):
        markdown = "This is **bold** and *italic* and `code`."
        node = markdown_to_html_node(markdown)
        self.assertEqual(
            node.to_html(),
            "<div><p>This is <b>bold</b> and <i>italic</i> and <code>code</code>.</p></div>"
        )


    def test_ordered_list(self):
        markdown = """1. First
2. Second
3. Third"""
        node = markdown_to_html_node(markdown)
        self.assertEqual(
            node.to_html(),
            "<div><ol><li>First</li><li>Second</li><li>Third</li></ol></div>"
        )

    def test_multiple_heading_levels(self):
        markdown = """# Heading 1
## Heading 2
### Heading 3"""
        node = markdown_to_html_node(markdown)
        self.assertEqual(
            node.to_html(),
            "<div><h1>Heading 1</h1><h2>Heading 2</h2><h3>Heading 3</h3></div>"
        )

    def test_complex_formatting(self):
        markdown = """> This is a **bold** quote with `code`
* List item with *italic* text"""
        node = markdown_to_html_node(markdown)
        self.assertEqual(
            node.to_html(),
            "<div><blockquote>This is a <b>bold</b> quote with <code>code</code></blockquote><ul><li>List item with <i>italic</i> text</li></ul></div>"
        )

    def test_empty_input(self):
        node = markdown_to_html_node("")
        self.assertEqual(
            node.to_html(),
            "<div></div>"
        )

    def test_simple_paragraph(self):
        markdown = "This is a paragraph"
        result = markdown_to_blocks(markdown)  # Check block segmentation
        print("Blocks:", result)  # Debug print to inspect the returned blocks
        node = markdown_to_html_node(markdown)
        print("HTML Output:", node.to_html())  # Debug print to inspect generated HTML
        self.assertEqual(
            node.to_html(),
            "<div><p>This is a paragraph</p></div>"
        )


if __name__ == '__main__':
    unittest.main()