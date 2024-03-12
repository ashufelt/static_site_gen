import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_no_props_to_html(self):
        node = HTMLNode("p", "text_value", [], {})
        self.assertEqual("", node.props_to_html())
    
    def test_one_prop_to_html(self):
        node = HTMLNode("p", "text_value", [], {"href":"example.com"})
        self.assertEqual(" href=example.com", node.props_to_html())

    def test_three_props_to_html(self):
        node = HTMLNode("p", "text_value", [], {"href":"example.com", "style":"HDR", "quality":"HD"})
        self.assertEqual(" href=example.com style=HDR quality=HD", node.props_to_html())