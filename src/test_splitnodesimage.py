import unittest

from textnode import TextNode
from main import split_nodes_image, TextType

class TestSplitNodesImage(unittest.TestCase):
    def test_one_node_no_image(self):
        test_node = TextNode("This text has no image", TextType.text_type_text, None)
        expected_nodes = [TextNode("This text has no image", TextType.text_type_text, None)]
        self.assertEqual(expected_nodes, split_nodes_image([test_node]))
    
    def test_one_node_one_image(self):
        test_node = TextNode("This text has ![one image](example.com) in it", TextType.text_type_text, None)
        expected_nodes = [
            TextNode("This text has ", TextType.text_type_text, None), 
            TextNode("one image", TextType.text_type_image, "example.com"),
            TextNode(" in it", TextType.text_type_text, None)
        ]
        self.assertEqual(expected_nodes, split_nodes_image([test_node]))

    def test_one_node_two_images(self):
        test_node = TextNode("This is text with a ![first image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)", TextType.text_type_text, None)
        expected_nodes = [
            TextNode("This is text with a ", TextType.text_type_text, None),
            TextNode("first image", TextType.text_type_image, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextType.text_type_text, None),
            TextNode("second image", TextType.text_type_image, "https://i.imgur.com/3elNhQu.png"),
        ]
        self.assertEqual(expected_nodes, split_nodes_image([test_node]))

    def test_two_nodes_none_and_one(self):
        test_node_1 = TextNode("This text has no image", TextType.text_type_text, None)
        test_node_2 = TextNode("This text has ![one image](example.com) in it", TextType.text_type_text, None)
        expected_nodes = [
            TextNode("This text has no image", TextType.text_type_text, None),
            TextNode("This text has ", TextType.text_type_text, None), 
            TextNode("one image", TextType.text_type_image, "example.com"),
            TextNode(" in it", TextType.text_type_text, None)
        ]
        self.assertEqual(expected_nodes, split_nodes_image([test_node_1, test_node_2]))