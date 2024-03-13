from textnode import TextNode
from htmlnode import HTMLNode, ParentNode, LeafNode
from enum import Enum

class TextType():
    text_type_text = "text"
    text_type_bold = "bold"
    text_type_italic = "italic"
    text_type_code = "code"
    text_type_link = "link"
    text_type_image = "image"

def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.text_type_text:
        return LeafNode(None, text_node.value, None)
    if text_node.text_type == TextType.text_type_bold:
        return LeafNode("b", text_node.value, None)
    if text_node.text_type == TextType.text_type_italic:
        return LeafNode("i", text_node.value, None)
    if text_node.text_type == TextType.text_type_code:
        return LeafNode("code", text_node.value, None)
    if text_node.text_type == TextType.text_type_link:
        return LeafNode("a", text_node.value, {"href":text_node.url})
    if text_node.text_type == TextType.text_type_image:
        return LeafNode("img", "", {"src":text_node.url, "alt":text_node.value})
    raise ValueError("Invalid text node type")

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    if delimiter is null or delimiter == "":
        raise ValueError("Invalid delimiter")
    for node in old_nodes:


def main():
    example_node = TextNode("This is a test node", "bold", "https://www.boot.dev")
    print(example_node)
    # print("Hello world")


main()
