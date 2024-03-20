import re

from textnode import TextType, TextNode, text_to_textnodes

class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        props_string = ""
        if self.props is None:
            return props_string
        for prop, val in self.props.items():
            props_string += f" {prop}=\"{val}\""
        return props_string
    
    '''
    def __eq__(self, other_node):
        if self.tag != other_node.tag:
            return False
        if self.value != other_node.value:
            return False
        if len(self.children) != len(other_node.children):
            return False
        if self.props != other_node.props:
            return False
        for i in range(len(self.children)):
            if self.children[i] != other_node.children[i]:
                return False
        return True
    

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    '''

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
    
    def to_html(self):
        if self.value is None:
            raise ValueError("Leaf node must have a value")
        if self.tag is None:
            return self.value
        html_props = self.props_to_html()
        return f"<{self.tag}{html_props}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("Parent node must have a tag")
        if self.children is None or len(self.children) == 0:
            raise ValueError("Parent node must have children")
        html_string = f"<{self.tag}{self.props_to_html()}>\n"
        for child in self.children:
            html_string += "\n" + child.to_html()
        html_string += f"</{self.tag}>"
        return html_string
    
    def __repr__(self):
        return f"ParentNode({self.tag}, {self.children}, {self.props})"


def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.text_type_text:
        return LeafNode(None, text_node.text, None)
    if text_node.text_type == TextType.text_type_bold:
        return LeafNode("b", text_node.text, None)
    if text_node.text_type == TextType.text_type_italic:
        return LeafNode("i", text_node.text, None)
    if text_node.text_type == TextType.text_type_code:
        return LeafNode("code", text_node.text, None)
    if text_node.text_type == TextType.text_type_link:
        return LeafNode("a", text_node.text, {"href":text_node.url})
    if text_node.text_type == TextType.text_type_image:
        return LeafNode("img", "", {"src":text_node.url, "alt":text_node.text})
    raise ValueError("Invalid text node type")

class BlockType():
    paragraph = "paragraph"
    heading = "heading"
    code = "code"
    quote = "quote"
    u_list = "unordered_list"
    o_list = "ordered_list"

def markdown_to_html_node(markdown):
    markdown_blocks = markdown_to_blocks(markdown)
    top_children = []
    for block in markdown_blocks:
        top_children.append(block_to_html_node(block))
    return ParentNode("div", top_children, None)

def markdown_to_blocks(markdown):
    final_blocks = []
    initial_split_blocks = markdown.split("\n\n")
    for block in initial_split_blocks:
        if len(block) == 0:
            continue
        final_blocks.append(str.strip(block))
    return final_blocks

def block_to_html_node(markdown_block):
    block_type = block_to_block_type(markdown_block)
    if block_type == BlockType.paragraph:
        return LeafNode("p", value_to_inline_html(markdown_block.strip()), None)
    if block_type == BlockType.heading:
        heading_level = get_heading_level(markdown_block)
        heading_tag = f"h{heading_level}"
        return LeafNode(heading_tag, (markdown_block.strip("#").strip()), None)
    if block_type == BlockType.code:
        return block_to_code_htmlnode(markdown_block)
    if block_type == BlockType.quote:
        return block_to_blockquote_htmlnode(markdown_block)
    if block_type == BlockType.u_list:
        return block_to_u_list_htmlnode(markdown_block)
    if block_type == BlockType.o_list:
        return block_to_o_list_htmlnode(markdown_block)

def block_to_block_type(markdown):
    if re.match(r"^\#{1,6} [^\s]+.*$", markdown, flags=re.M) != None:
        return BlockType.heading
    if re.match(r"^```(.|\n)*``` *$", markdown) != None:
        return BlockType.code
    if check_markdown_for_quote_block(markdown):
        return BlockType.quote
    if check_markdown_for_u_list(markdown):
        return BlockType.u_list
    if check_markdown_for_o_list(markdown):
        return BlockType.o_list
    return BlockType.paragraph

# This function assumes that "heading" is a single line of text, beginning with 1 to 6 *s
def get_heading_level(heading):
    count =  0
    for letter in heading:
        if letter == '#':
            count += 1
        else:
            return count
    return count

# This function assumes that markdown_block is a valid code block in markdown
def block_to_code_htmlnode(markdown_block):
    node_value = ""
    lines = markdown_block.splitlines()
    for line in lines:
        potential_new_line = line.strip("`").strip()
        if len(potential_new_line) > 0:
            node_value += potential_new_line + '\n'
    inner_node = LeafNode("code", (node_value[0:-1]), None)
    return ParentNode("pre", [inner_node], None)

# This function assumes that markdown_block is a valid blockquote in markdown
def block_to_blockquote_htmlnode(markdown_block):
    node_value = ""
    lines = markdown_block.splitlines()
    for line in lines:
        node_value += line.strip(">").strip() + '\n'
    return LeafNode("blockquote", (node_value[0:-1]), None)

# This function assumes that markdown_block is a valid unordered list in markdown
def block_to_u_list_htmlnode(markdown_block):
    list_items = []
    lines = markdown_block.splitlines()
    for line in lines:
        text = line.strip("*-").strip()
        list_items.append(LeafNode("li", (text), None))
    return ParentNode("ul", list_items, None)

# This function assumes that markdown_block is a valid ordered list in markdown
def block_to_o_list_htmlnode(markdown_block):
    list_items = []
    lines = markdown_block.splitlines()
    for line in lines:
        text = line.split(".", 1)[1].strip()
        list_items.append(LeafNode("li", (text), None))
    return ParentNode("ol", list_items, None)

def check_markdown_for_quote_block(markdown):
    lines = markdown.splitlines()
    if len(lines) == 0:
        return False
    for line in lines:
        if line[0] != '>':
            return False
    return True

def check_markdown_for_u_list(markdown):
    lines = markdown.splitlines()
    if len(lines) == 0:
        return False
    for line in lines:
        if line[0:2] != '* ' and line[0:2] != '- ':
            return False
    return True

def check_markdown_for_o_list(markdown):
    lines = markdown.splitlines()
    # print(lines)
    if len(lines) == 0:
        return False
    for i in range(len(lines)):
        lineNum = i+1
        if lines[i][0] != f"{lineNum}":
            # print(f"{lines[i][0]} != {lineNum}")
            return False
        if lines[i].removeprefix(f"{lineNum}")[0] != '.':
            # print(f"{lines[i].removeprefix(f"{lineNum}")[0]}")
            return False
    return True

def extract_title(markdown):
    markdown_blocks = markdown_to_blocks(markdown)
    title = ""
    for block in markdown_blocks:
        node = block_to_html_node(block)
        if node.tag == "h1":
            title = node.value
            break
    if title == "":
        raise ValueError("Markdown does not contain a top header (h1, '* Example H1')")
    return title

def value_to_inline_html(text):
    text_nodes = text_to_textnodes(text)
    leaf_value = ""
    for node in text_nodes:
        leaf_node = text_node_to_html_node(node)
        leaf_value += leaf_node.to_html()
    return leaf_value