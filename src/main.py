from textnode import TextNode
from htmlnode import HTMLNode, ParentNode, LeafNode
from enum import Enum
import re

class TextType():
    text_type_text = "text"
    text_type_bold = "bold"
    text_type_italic = "italic"
    text_type_code = "code"
    text_type_link = "link"
    text_type_image = "image"

text_type_delims = {
    "bold": "**",
    "italic": "*",
    "code": "`"
}

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
    if delimiter is None or delimiter == "":
        raise ValueError("Invalid delimiter: Cannot be None or empty")
    new_nodes = []
    for node in old_nodes:
        if not isinstance(node, TextNode):
            new_nodes.append(node)
        else:
            new_nodes.extend(split_one_node(node, delimiter, text_type))
    return new_nodes


def split_one_node(node, delimiter, text_type):
    new_nodes = []
    if delimiter != text_type_delims[text_type]:
        raise ValueError(f"Delimiter:{delimiter} does not match intended text type:{text_type}")
    sections = []
    if delimiter == "*":
        sections = re.split(r"(?<!\*)\*(?!\*)", node.text)
    else:
        sections = node.text.split(delimiter)
    if len(sections) % 2 != 1:
        raise ValueError("Matching closing delimiter not found for all opening delimiters")
    for i in range(len(sections)):
        if len(sections[i]) == 0:
            continue
        if i % 2 == 0:
            new_nodes.append(TextNode(sections[i], TextType.text_type_text, node.url))
        else:
            new_nodes.append(TextNode(sections[i], text_type, node.url))
    return new_nodes


def main():
    example_node = TextNode("This is a test node", "bold", "https://www.boot.dev")
    # print(example_node)
    # print("Hello world")


main()
