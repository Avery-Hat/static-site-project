import unittest
from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        # Test with no properties
        node = HTMLNode()
        self.assertEqual(node.props_to_html(), "")

        # Test with one property
        node = HTMLNode(props={"href": "https://google.com"})
        self.assertEqual(node.props_to_html(), ' href="https://google.com"')

        # Test with multiple properties
        node = HTMLNode(props={
            "href": "https://google.com",
            "target": "_blank"
        })
        self.assertEqual(
            node.props_to_html(),
            ' href="https://google.com" target="_blank"'
        )

    def test_constructor(self):
        # Test all parameters being None (default case)
        node = HTMLNode()
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)

        # Test with all parameters provided
        node = HTMLNode("p", "Hello", [], {"class": "greeting"})
        self.assertEqual(node.tag, "p")
        self.assertEqual(node.value, "Hello")
        self.assertEqual(node.children, [])
        self.assertEqual(node.props, {"class": "greeting"})
    
    def test_repr(self):
        node = HTMLNode(
            "div",
            "Hello",
            [],
            {"class": "greeting", "id": "hello"}
        )
        expected_string = "HTMLNode(tag: div, value: Hello, children: [], props: {'class': 'greeting', 'id': 'hello'})"
        self.assertEqual(repr(node), expected_string)

class TestLeafNode(unittest.TestCase):
    def test_basic_html_rendering(self):
        # Test rendering with a tag and value
        leaf = LeafNode("p", "This is a paragraph.")
        self.assertEqual(leaf.to_html(), "<p>This is a paragraph.</p>")

        leaf = LeafNode("a", "Click here", {"href": "https://google.com"})
        self.assertEqual(leaf.to_html(), '<a href="https://google.com">Click here</a>')

    def test_raw_text_rendering(self):
        # Test rendering with no tag
        raw_text_leaf = LeafNode(None, "This is plain text.")
        self.assertEqual(raw_text_leaf.to_html(), "This is plain text.")

    def test_missing_value_raises_error(self):
        # Test that a missing value raises a ValueError
        with self.assertRaises(ValueError) as context:
            leaf = LeafNode("p", None)
            leaf.to_html()
        self.assertEqual(str(context.exception), "All LeafNodes must have a value!")

    def test_empty_props(self):
        # Test rendering with an empty props dictionary
        leaf = LeafNode("div", "Empty props test")
        self.assertEqual(leaf.to_html(), "<div>Empty props test</div>")

        # Test with no tag but non-empty value, which should render as raw text
        raw_text_leaf = LeafNode(None, "Raw text only")
        self.assertEqual(raw_text_leaf.to_html(), "Raw text only")
        
    def test_none_props(self):
        # Test when props are None
        leaf = LeafNode("p", "Test with None props", None)
        self.assertEqual(leaf.to_html(), "<p>Test with None props</p>")


if __name__ == "__main__":
    unittest.main()