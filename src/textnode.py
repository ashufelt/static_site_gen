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
