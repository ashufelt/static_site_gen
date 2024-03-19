import unittest

from textnode import TextNode, split_nodes_link, TextType

class TestSplitNodesLink(unittest.TestCase):
    def test_one_node_no_link(self):
        test_node = TextNode("This text has no link", TextType.text_type_text, None)
        expected_nodes = [TextNode("This text has no link", TextType.text_type_text, None)]
        self.assertEqual(expected_nodes, split_nodes_link([test_node]))
    
    def test_one_node_one_link(self):
        test_node = TextNode("This text has [one link](example.com) in it", TextType.text_type_text, None)
        expected_nodes = [
            TextNode("This text has ", TextType.text_type_text, None), 
            TextNode("one link", TextType.text_type_link, "example.com"),
            TextNode(" in it", TextType.text_type_text, None)
        ]
        self.assertEqual(expected_nodes, split_nodes_link([test_node]))
    
    def test_one_node_two_links(self):
        test_node = TextNode("This is text with a [first link](https://i.imgur.com/zjjcJKZ.png) and another [second link](https://i.imgur.com/3elNhQu.png)", TextType.text_type_text, None)
        expected_nodes = [
            TextNode("This is text with a ", TextType.text_type_text, None),
            TextNode("first link", TextType.text_type_link, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextType.text_type_text, None),
            TextNode("second link", TextType.text_type_link, "https://i.imgur.com/3elNhQu.png"),
        ]
        self.assertEqual(expected_nodes, split_nodes_link([test_node]))
    
    def test_two_nodes_none_and_one(self):
        test_node_1 = TextNode("This text has no link", TextType.text_type_text, None)
        test_node_2 = TextNode("This text has [one link](example.com) in it", TextType.text_type_text, None)
        expected_nodes = [
            TextNode("This text has no link", TextType.text_type_text, None),
            TextNode("This text has ", TextType.text_type_text, None), 
            TextNode("one link", TextType.text_type_link, "example.com"),
            TextNode(" in it", TextType.text_type_text, None)
        ]
        self.assertEqual(expected_nodes, split_nodes_link([test_node_1, test_node_2]))