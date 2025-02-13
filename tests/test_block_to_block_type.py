#located in markdown_parser.py
import unittest
from markdown_parser import block_to_block_type

class TestBlockToBlockType(unittest.TestCase):
    def test_heading(self):
        self.assertEqual(block_to_block_type("# Heading"), "heading")
        self.assertEqual(block_to_block_type("#Invalid"), "paragraph")  # no space after #
        self.assertEqual(block_to_block_type("####### Too many"), "paragraph")  # 7 #'s
    
    def test_unordered_list(self):
        self.assertEqual(block_to_block_type("* Item 1\n* Item 2"), "unordered_list")
        self.assertEqual(block_to_block_type("- Item 1\n- Item 2"), "unordered_list")
        self.assertEqual(block_to_block_type("*Invalid"), "paragraph")  # no space after *
    
    def test_ordered_list(self):
        self.assertEqual(block_to_block_type("1. First\n2. Second"), "ordered_list")
        self.assertEqual(block_to_block_type("1. First\n3. Wrong number"), "paragraph")

    
    def test_code_block(self):
        self.assertEqual(block_to_block_type("```\ncode here\n```"), "code")
        self.assertEqual(block_to_block_type("````\ncode here\n````"), "paragraph")  # too many backticks
        self.assertEqual(block_to_block_type("```\ncode here"), "paragraph")  # missing closing backticks
    
    def test_quote_block(self):
        self.assertEqual(block_to_block_type("> Quote line 1\n> Quote line 2"), "quote")
        self.assertEqual(block_to_block_type(">Quote line 1\n>Quote line 2"), "quote")  # no space after >
        self.assertEqual(block_to_block_type("> Quote\nNot a quote"), "paragraph")  # mixed content
    
    def test_empty_block(self):
        self.assertEqual(block_to_block_type(""), "paragraph")  # completely empty
        self.assertEqual(block_to_block_type(" "), "paragraph")  # just a space
        self.assertEqual(block_to_block_type("\n\n"), "paragraph")  # just newlines
        self.assertEqual(block_to_block_type("   \n  \n  "), "paragraph")  # spaces and newlines
        
if __name__ == '__main__':
    unittest.main()