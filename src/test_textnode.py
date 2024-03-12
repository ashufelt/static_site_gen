import unittest

from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
    
    def test_url_none(self):
        node = TextNode("equal", "bold", None)
        node2 = TextNode("equal", "bold", None)
        self.assertEqual(node, node2)

    def test_text_dif(self):
        node = TextNode("not equal", "bold", "url")
        node2 = TextNode("not", "bold", "url")
        self.assertNotEqual(node, node2)
    
    def test_type_dif(self):
        node = TextNode("equal", "bold", "url")
        node2 = TextNode("equal", "italic", "url")
        self.assertNotEqual(node, node2)
    
    def test_url_dif(self):
        node = TextNode("equal", "bold", "url")
        node2 = TextNode("equal", "bold", "url_different")
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()