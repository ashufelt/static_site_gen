import re

class TextNode:
    def __init__(self,text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other_node):
        # print("Testing equality")
        if other_node.text != self.text:
            return False
        if other_node.text_type != self.text_type:
            return False
        if ((self.url is None) != (other_node.url is None)) or (other_node.url != self.url):
            return False
        return True

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"


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

def text_to_textnodes(text):
    initial_textnode = TextNode(text, TextType.text_type_text, None)
    nodes_split_on_bold = split_nodes_delimiter([initial_textnode], "**", TextType.text_type_bold)
    nodes_split_on_italic = split_nodes_delimiter(nodes_split_on_bold, "*", TextType.text_type_italic)
    nodes_split_on_code = split_nodes_delimiter(nodes_split_on_italic, "`", TextType.text_type_code)
    nodes_split_on_image = split_nodes_image(nodes_split_on_code)
    nodes_split_on_link = split_nodes_link(nodes_split_on_image)
    return nodes_split_on_link

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    if delimiter is None or delimiter == "":
        raise ValueError("Invalid delimiter: Cannot be None or empty")
    new_nodes = []
    for node in old_nodes:
        if not isinstance(node, TextNode):
            new_nodes.append(node)
        elif node.text_type != TextType.text_type_text:
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

def split_nodes_image(old_nodes):
    # print(f"Splitting nodes: {old_nodes}")
    new_nodes = []
    for node in old_nodes:
        original_text = node.text
        # print(original_text)
        if original_text == "":
            continue
        images = extract_markdown_images(original_text)
        if images == []:
            new_nodes.append(node)
            continue
        splits_first_image = original_text.split(f"![{images[0][0]}]({images[0][1]})", 1)
        # print(splits_first_image)
        if splits_first_image != "":
            new_nodes.append(TextNode(splits_first_image[0], TextType.text_type_text, None))
        new_nodes.append(TextNode(images[0][0], TextType.text_type_image, images[0][1]))
        new_nodes.extend(split_nodes_image([TextNode(splits_first_image[1], TextType.text_type_text, None)]))
    return new_nodes
        

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        original_text = node.text
        if original_text == "":
            continue
        links = extract_markdown_links(original_text)
        if links == []:
            new_nodes.append(node)
            continue
        splits_first_link = original_text.split(f"[{links[0][0]}]({links[0][1]})", 1)
        if splits_first_link != "":
            new_nodes.append(TextNode(splits_first_link[0], TextType.text_type_text, None))
        new_nodes.append(TextNode(links[0][0], TextType.text_type_link, links[0][1]))
        new_nodes.extend(split_nodes_link([TextNode(splits_first_link[1], TextType.text_type_text, None)]))
    return new_nodes

# returns list of tuples of images, in form [(alt_text, link), ...]
def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

# returns list of tuples of links, in form [(link_text, link), ...]
def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)