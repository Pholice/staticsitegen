import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode("p", "Hello World", [], {"class": "example"})
        expected_repr = "HTMLNode:(p, Hello World, [], {'class': 'example'})"
        self.assertEqual(node.__repr__(), expected_repr)
    def test_neq(self):
        node = HTMLNode("<h2>", "Hello World", [], {"href": "https://www.google.com"})
        node2 = HTMLNode("<p>", "Hello World", [], {"href": "https://www.google.com"})
        self.assertNotEqual(node, node2)
    def test_props_to_html(self):
        node = HTMLNode("<p>", "Hello World", [], {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode("p", "This is a paragraph of text.")
        expected_repr = "<p>This is a paragraph of text.</p>"
        node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        expected_repr2 = '<a href="https://www.google.com">Click me!</a>'
        self.assertEqual(node.to_html(), expected_repr)
        self.assertEqual(node2.to_html(), expected_repr2)

# Parent Test Cases from Boot.Dev
class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )

if __name__ == "__main__":
    unittest.main()
