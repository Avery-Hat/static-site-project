import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode
from textnode import TextNode, TextType
from text_to_html import text_node_to_html_node

class TestTextToHTML(unittest.TestCase):
    def test_text_tohtml(self):
        node = TextNode("hello", TextType.TEXT)
        result = text_node_to_html_node(node)
        self.assertIsInstance(result, LeafNode)  # Check if it's a LeafNode
        self.assertIsNone(result.tag)           # Check if tag is None
        self.assertEqual(result.value, "hello") # Check if value matches
    
    def test_bold_tohtml(self):
        node = TextNode("deez", TextType.BOLD)
        result = text_node_to_html_node(node)
        self.assertIsInstance(result, LeafNode)
        self.assertEqual(result.tag, "b")
        self.assertEqual(result.value, "deez")

    def test_italic_tohtml(self):
        node = TextNode("nuts", TextType.ITALIC)
        result = text_node_to_html_node(node)
        self.assertIsInstance(result, LeafNode)
        self.assertEqual(result.tag,"i")
        self.assertEqual(result.value,"nuts")
    
    def test_code_tohtml(self):
        node = TextNode("print('deeznuts')", TextType.CODE)
        result = text_node_to_html_node(node)
        self.assertIsInstance(result, LeafNode)
        self.assertEqual(result.tag,"code")
        self.assertEqual(result.value,"print('deeznuts')")

    def test_image_tohtml(self):
        node = TextNode("veriah_heart_glasses.png", TextType.IMAGE, "Veriah wearing heart glasses")
        result = text_node_to_html_node(node)
        self.assertIsInstance(result, LeafNode)
        self.assertEqual(result.tag, "img")
        self.assertEqual(result.value, "")  # empty string value
        self.assertEqual(result.props["src"], "veriah_heart_glasses.png")
        self.assertEqual(result.props["alt"], "Veriah wearing heart glasses")

    def test_link_tohtml(self):
        # TextNode for links needs both url and display text
        node = TextNode("Click to see cat bread", TextType.LINK, "https://imgur.com/gallery/cat-bread-OUlXd")
        result = text_node_to_html_node(node)
        self.assertIsInstance(result, LeafNode)
        self.assertEqual(result.tag, "a")
        self.assertEqual(result.value, "Click to see cat bread")  # The visible text
        self.assertEqual(result.props["href"], "https://imgur.com/gallery/cat-bread-OUlXd") 

    def test_invalid_type_tohtml(self):
        node = TextNode("bwana", "NOT_A_TYPE")
        with self.assertRaises(Exception):
            result = text_node_to_html_node(node)


if __name__ == "__main__":
    unittest.main()