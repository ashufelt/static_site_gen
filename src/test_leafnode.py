import unittest

from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_no_tag(self):
        node = LeafNode(None, "This leaf has no tag")
        self.assertEqual("This leaf has no tag", node.to_html())
    
    def test_no_tag_with_props(self):
        node = LeafNode(None, "This leaf has no tag, so props shouldn't show", {"href":"example.com"})
        self.assertEqual("This leaf has no tag, so props shouldn't show", node.to_html())
    
    def test_tag_no_props(self):
        node = LeafNode("p", "A paragraph")
        self.assertEqual("<p>A paragraph</p>", node.to_html())
    
    def test_tag_with_props(self):
        node = LeafNode("a", "A link", {"href":"example.com"})
        self.assertEqual("<a href=example.com>A link</a>", node.to_html())