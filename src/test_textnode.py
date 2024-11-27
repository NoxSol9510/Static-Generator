import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_url(self):
        node = TextNode("Click here", TextType.TEXT, "http://example.com")
        self.assertEqual(node.url, "http://example.com")

    def test_ineq(self):
        node = TextNode("Hello", TextType.BOLD)
        node2 = TextNode("Hello", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_diftext(self):
        node = TextNode("Hi", TextType.TEXT)
        node2 = TextNode("Hi", TextType.TEXT)
        self.assertEqual(node, node2)
    
    def test_it(self):
        node = TextNode("Hi", TextType.ITALIC)
        node2 = TextNode("Hi", TextType.ITALIC)
        self.assertEqual(node, node2)


if __name__ == "__main__":
    unittest.main()