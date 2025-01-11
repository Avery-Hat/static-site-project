import unittest

from textnode import TextNode, TextType # variables for tests located in src

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_url(self):
        node = TextNode("Testing None url...", TextType.BOLD, url=None)
        node2 = TextNode("Testing None url...", TextType.BOLD, url=None)
        self.assertEqual(node, node2) # Expectation: They are not equal if URL affects equality
    
    def test_different_text_type(self):
        node = TextNode("Same text, different type", TextType.BOLD)
        node2 = TextNode("Same text, different type", TextType.ITALIC)
        self.assertNotEqual(node, node2)  # Expectation: They are not equal if text_type affects equality.

    def test_different_text(self):
        node = TextNode("Text difference", TextType.BOLD)
        node2 = TextNode("Another text difference", TextType.BOLD)
        self.assertNotEqual(node, node2)  # Expectation: They are not equal if text affects equality.


if __name__ == "__main__":
    unittest.main()