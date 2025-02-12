import unittest
from markdown_parser import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):
    def test_basic_block_separation(self):
        test_markdown = """# Heading
This is a paragraph.

* List item 1
* List item 2"""
        result = markdown_to_blocks(test_markdown)
        self.assertEqual(len(result), 2)
        self.assertEqual(result[0], "# Heading\nThis is a paragraph.")
        self.assertEqual(result[1], "* List item 1\n* List item 2")

    def test_extra_whitespace(self):
        test_markdown = """   # Heading   

    This has spaces    

* List"""
        result = markdown_to_blocks(test_markdown)
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0], "# Heading")

    def test_multiple_blank_lines(self):
        test_markdown = """# Heading


This has extra blank lines


* List"""
        result = markdown_to_blocks(test_markdown)
        self.assertEqual(len(result), 3)

    def test_empty_string(self):
        test_markdown = ""
        result = markdown_to_blocks(test_markdown)
        self.assertEqual(len(result), 0)
        self.assertEqual(result, [])

    def test_single_line(self):
        test_markdown = "Just one line of text"
        result = markdown_to_blocks(test_markdown)
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0], "Just one line of text")

    def test_only_whitespace(self):
        test_markdown = """

            

        """
        result = markdown_to_blocks(test_markdown)
        self.assertEqual(len(result), 0)
        self.assertEqual(result, [])

if __name__ == '__main__':
    unittest.main()