import unittest

from textnode import TextNode, TextType, split_nodes_image, split_nodes_link
# variables for tests located in src
# Add split_nodes_image to import

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

class TestSplitNodeImaging(unittest.TestCase):
    def test_split_nodes_image(self):
        # Test 1: No images
        node = TextNode("Just plain text", TextType.TEXT)
        nodes = split_nodes_image([node])
        self.assertEqual(len(nodes), 1)
        self.assertEqual(nodes[0], node)

        # Test 2: Single Frank
        node = TextNode("Hello ![Frank the Turtle](https://i.imgur.com/VlIywV2.jpeg) world", TextType.TEXT)
        nodes = split_nodes_image([node])
        self.assertEqual(len(nodes), 3)
        self.assertEqual(nodes[0].text, "Hello ")
        self.assertEqual(nodes[1].text_type, TextType.IMAGE)
        self.assertEqual(nodes[1].source_path, "https://i.imgur.com/VlIywV2.jpeg")
        self.assertEqual(nodes[1].alt_text, "Frank the Turtle")
        self.assertEqual(nodes[2].text, " world")

        # Test 3: Multiple Franks
        node = TextNode(
            "![Frank](https://i.imgur.com/VlIywV2.jpeg) says hi to ![Frank again](https://i.imgur.com/VlIywV2.jpeg)",
            TextType.TEXT
        )
        nodes = split_nodes_image([node])
        self.assertEqual(len(nodes), 3)
        self.assertEqual(nodes[0].text_type, TextType.IMAGE)
        self.assertEqual(nodes[0].source_path, "https://i.imgur.com/VlIywV2.jpeg")

class TestSplitNodeLink(unittest.TestCase):
    def test_split_nodes_link(self):  # Add self parameter
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT,
        )
        nodes = split_nodes_link([node])
        # Use self.assert... instead of assert
        self.assertEqual(len(nodes), 4)
        self.assertEqual(nodes[0].text, "This is text with a link ")
        self.assertEqual(nodes[0].text_type, TextType.TEXT)
        self.assertEqual(nodes[1].text, "to boot dev")
        self.assertEqual(nodes[1].text_type, TextType.LINK)
        self.assertEqual(nodes[1].url, "https://www.boot.dev")
        self.assertEqual(nodes[2].text, " and ")
        self.assertEqual(nodes[2].text_type, TextType.TEXT)
        self.assertEqual(nodes[3].text, "to youtube")
        self.assertEqual(nodes[3].text_type, TextType.LINK)
        self.assertEqual(nodes[3].url, "https://www.youtube.com/@bootdotdev")

    def test_no_links(self):
        node = TextNode("Just plain text", TextType.TEXT)
        nodes = split_nodes_link([node])
        self.assertEqual(len(nodes), 1)
        self.assertEqual(nodes[0], node)

    def test_link_at_start(self):
        node = TextNode(
            "[boot.dev](https://boot.dev) is a great learning platform",
            TextType.TEXT
        )
        nodes = split_nodes_link([node])
        self.assertEqual(len(nodes), 2)
        self.assertEqual(nodes[0].text, "boot.dev")
        self.assertEqual(nodes[0].text_type, TextType.LINK)
        self.assertEqual(nodes[0].url, "https://boot.dev")
        self.assertEqual(nodes[1].text, " is a great learning platform")
        self.assertEqual(nodes[1].text_type, TextType.TEXT)

    def test_link_at_end(self):
        node = TextNode(
            "Learn to code at [boot.dev](https://boot.dev)",
            TextType.TEXT
        )
        nodes = split_nodes_link([node])
        self.assertEqual(len(nodes), 2)
        self.assertEqual(nodes[0].text, "Learn to code at ")
        self.assertEqual(nodes[0].text_type, TextType.TEXT)
        self.assertEqual(nodes[1].text, "boot.dev")
        self.assertEqual(nodes[1].text_type, TextType.LINK)
        self.assertEqual(nodes[1].url, "https://boot.dev")

if __name__ == "__main__":
    unittest.main()