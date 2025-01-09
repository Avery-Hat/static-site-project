import unittest
from htmlnode import HTMLNode

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

if __name__ == "__main__":
    unittest.main()