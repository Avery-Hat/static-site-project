import unittest
from src.textnode import TextNode, TextType
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
        assert len(new_nodes) == 8
        
        # Check each node's text and type
        assert new_nodes[0].text == "This is "
        assert new_nodes[1].text == "code"
        assert new_nodes[2].text == ""
        assert new_nodes[3].text == "already bold"
        assert new_nodes[4].text == "More "
        assert new_nodes[5].text == "code"
        assert new_nodes[6].text == " here"
        assert new_nodes[7].text == "plain text"
        assert new_nodes[8].text == ""
        assert new_nodes[9].text == "final code"
        assert new_nodes[10].text == ""

        # Check types of converted nodes
        assert new_nodes[1].text_type == TextType.CODE
        assert new_nodes[3].text_type == TextType.BOLD  # unchanged
        assert new_nodes[5].text_type == TextType.CODE
        assert new_nodes[9].text_type == TextType.CODE

if __name__ == "__main__":
    unittest.main()