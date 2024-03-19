import unittest

from textnode import TextNode, text_to_textnodes, TextType

class TestTextToTextNodes(unittest.TestCase):
    def test_bootdev_example(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://boot.dev)"
        expected_nodes = [
            TextNode("This is ", TextType.text_type_text),
            TextNode("text", TextType.text_type_bold),
            TextNode(" with an ", TextType.text_type_text),
            TextNode("italic", TextType.text_type_italic),
            TextNode(" word and a ", TextType.text_type_text),
            TextNode("code block", TextType.text_type_code),
            TextNode(" and an ", TextType.text_type_text),
            TextNode("image", TextType.text_type_image, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and a ", TextType.text_type_text),
            TextNode("link", TextType.text_type_link, "https://boot.dev")
        ]
        # text_to_textnodes(text)
        self.assertEqual(expected_nodes, text_to_textnodes(text))
    
    def test_bootdev_example_mixedup(self):
        text = "This is ![an image](https://i.imgur.com/zjjcJKZ.png) with a [link](https://boot.dev) and an *italic* word and a `code block` and **bold text**"
        expected_nodes = [
            TextNode("This is ", TextType.text_type_text),
            TextNode("an image", TextType.text_type_image, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" with a ", TextType.text_type_text),
            TextNode("link", TextType.text_type_link, "https://boot.dev"),
            TextNode(" and an ", TextType.text_type_text),
            TextNode("italic", TextType.text_type_italic),
            TextNode(" word and a ", TextType.text_type_text),
            TextNode("code block", TextType.text_type_code),
            TextNode(" and ", TextType.text_type_text),
            TextNode("bold text", TextType.text_type_bold)
        ]
        self.assertEqual(expected_nodes, text_to_textnodes(text))