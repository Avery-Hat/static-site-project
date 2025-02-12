import unittest
from textnode import TextNode, TextType
from split_nodes_delimiter import split_nodes_delimiter

class TestSplitNode(unittest.TestCase):
    def test_split_nodes_delimiter_basic(self):  # added self here
        node = TextNode("This is `code` here", TextType.TEXT)
        nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(len(nodes), 3)  # changed assert to self.assertEqual
        self.assertEqual(nodes[0].text, "This is ")
        self.assertEqual(nodes[1].text, "code")
        self.assertEqual(nodes[2].text, " here")
    
    def test_split_nodes_delimiter_no_delimiter(self):
        node = TextNode("Plain text", TextType.TEXT)
        nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        assert len(nodes) == 1
        assert nodes[0].text == "Plain text"

    def test_split_nodes_delimiter_invalid(self):
        node = TextNode("This text has `unclosed delimiter", TextType.TEXT)
        with self.assertRaises(ValueError):
            split_nodes_delimiter([node], "`", TextType.CODE)

    def test_split_nodes_delimiter_multiple_nodes(self):
        # Create a variety of nodes
        nodes = [
            TextNode("This is `code`", TextType.TEXT),
            TextNode("already bold", TextType.BOLD),
            TextNode("More `code` here", TextType.TEXT),
            TextNode("plain text", TextType.TEXT),
            TextNode("`final code`", TextType.TEXT)
        ]
        
        # Split them
        new_nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
        
        # Assert the results
        self.assertEqual(len(new_nodes), 8)
        
        # Check each node's text and type
        self.assertEqual(new_nodes[0].text, "This is ")
        self.assertEqual(new_nodes[1].text, "code")
        self.assertEqual(new_nodes[2].text, "already bold")
        self.assertEqual(new_nodes[3].text, "More ")
        self.assertEqual(new_nodes[4].text, "code")
        self.assertEqual(new_nodes[5].text, " here")
        self.assertEqual(new_nodes[6].text, "plain text")
        self.assertEqual(new_nodes[7].text, "final code")

        # Check types of converted nodes
        self.assertEqual(new_nodes[1].text_type, TextType.CODE)
        self.assertEqual(new_nodes[2].text_type, TextType.BOLD)  # unchanged
        self.assertEqual(new_nodes[4].text_type, TextType.CODE)
        self.assertEqual(new_nodes[7].text_type, TextType.CODE)

class TestBoldBoys(unittest.TestCase):
    def test_bold_no_surrounding_text(self):
        node = TextNode("**bold**", TextType.TEXT)
        nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(len(nodes), 1)
        self.assertEqual(nodes[0].text, "bold")
        self.assertEqual(nodes[0].text_type, TextType.BOLD)

    def test_bold_empty_middle(self):
        node = TextNode("Hello****World", TextType.TEXT)
        nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(len(nodes), 2)
        self.assertEqual(nodes[0].text, "Hello")
        self.assertEqual(nodes[1].text, "World")
        self.assertEqual(nodes[0].text_type, TextType.TEXT)
        self.assertEqual(nodes[1].text_type, TextType.TEXT)

if __name__ == "__main__":
    unittest.main()