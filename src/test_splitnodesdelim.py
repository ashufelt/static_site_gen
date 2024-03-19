import unittest

from textnode import TextNode, split_one_node, split_nodes_delimiter, TextType

class TestSplitNodesDelim(unittest.TestCase):
    def test_one_node_simple_bold(self):
        node_list = split_one_node(TextNode("This **word** is bold", TextType.text_type_text), "**", TextType.text_type_bold)
        self.assertEqual(3, len(node_list))
        self.assertEqual("TextNode(This , text, None)", f"{node_list[0]}")
        self.assertEqual("TextNode(word, bold, None)", f"{node_list[1]}")
        self.assertEqual("TextNode( is bold, text, None)", f"{node_list[2]}")

    def test_one_node_simple_italic(self):
        node_list = split_one_node(TextNode("This *word* is in italics", TextType.text_type_text), "*", TextType.text_type_italic)
        self.assertEqual(3, len(node_list))
        self.assertEqual("TextNode(This , text, None)", f"{node_list[0]}")
        self.assertEqual("TextNode(word, italic, None)", f"{node_list[1]}")
        self.assertEqual("TextNode( is in italics, text, None)", f"{node_list[2]}")

    def test_one_node_simple_code(self):
        node_list = split_one_node(TextNode("This `word` is code", TextType.text_type_text), "`", TextType.text_type_code)
        self.assertEqual(3, len(node_list))
        self.assertEqual("TextNode(This , text, None)", f"{node_list[0]}")
        self.assertEqual("TextNode(word, code, None)", f"{node_list[1]}")
        self.assertEqual("TextNode( is code, text, None)", f"{node_list[2]}")

    def test_one_node_no_closing_delimiter_bold(self):
        node = TextNode("There **is no closing bold delimiter", TextType.text_type_text)
        with self.assertRaises(ValueError):
            split_one_node(node, "**", TextType.text_type_italic)

    def test_one_node_no_closing_delimiter_italic(self):
        node = TextNode("There *is no closing italic delimiter", TextType.text_type_text)
        with self.assertRaises(ValueError):
            split_one_node(node, "*", TextType.text_type_italic)
    
    def test_one_node_no_closing_delimiter_code(self):
        node = TextNode("There `is no closing code delimiter", TextType.text_type_text)
        with self.assertRaises(ValueError):
            split_one_node(node, "`", TextType.text_type_italic)
    
    def test_one_node_delimiter_type_mismatch(self):
        node = TextNode("This isn't an 'italic' delimiter", TextType.text_type_text)
        with self.assertRaises(ValueError):
            split_one_node(node, "`", TextType.text_type_italic)
    
    def test_one_node_all_delims_only_split_bold(self):
        node_list = split_one_node(TextNode("This `example` *has* **all** the delims", TextType.text_type_text), "**", TextType.text_type_bold)
        self.assertEqual(3, len(node_list))
        self.assertEqual("TextNode(This `example` *has* , text, None)", f"{node_list[0]}")
        self.assertEqual("TextNode(all, bold, None)", f"{node_list[1]}")
        self.assertEqual("TextNode( the delims, text, None)", f"{node_list[2]}")
    
    def test_one_node_all_delims_only_split_italic(self):
        node_list = split_one_node(TextNode("This `example` *has* **all** the delims", TextType.text_type_text), "*", TextType.text_type_italic)
        self.assertEqual(3, len(node_list))
        self.assertEqual("TextNode(This `example` , text, None)", f"{node_list[0]}")
        self.assertEqual("TextNode(has, italic, None)", f"{node_list[1]}")
        self.assertEqual("TextNode( **all** the delims, text, None)", f"{node_list[2]}")
    
    def test_one_node_all_delims_only_split_code(self):
        node_list = split_one_node(TextNode("This `example` *has* **all** the delims", TextType.text_type_text), "`", TextType.text_type_code)
        self.assertEqual(3, len(node_list))
        self.assertEqual("TextNode(This , text, None)", f"{node_list[0]}")
        self.assertEqual("TextNode(example, code, None)", f"{node_list[1]}")
        self.assertEqual("TextNode( *has* **all** the delims, text, None)", f"{node_list[2]}")
    
    def test_one_node_bold_at_start(self):
        node_list = split_one_node(TextNode("**This** starts bold", TextType.text_type_text), "**", TextType.text_type_bold)
        self.assertEqual(2, len(node_list))
        self.assertEqual("TextNode(This, bold, None)", f"{node_list[0]}")
        self.assertEqual("TextNode( starts bold, text, None)", f"{node_list[1]}")
    
    def test_one_node_bold_at_end(self):
        node_list = split_one_node(TextNode("This ends **bold**", TextType.text_type_text), "**", TextType.text_type_bold)
        self.assertEqual(2, len(node_list))
        self.assertEqual("TextNode(This ends , text, None)", f"{node_list[0]}")
        self.assertEqual("TextNode(bold, bold, None)", f"{node_list[1]}")
    
    def test_one_node_italic_at_start(self):
        node_list = split_one_node(TextNode("*This* starts italic", TextType.text_type_text), "*", TextType.text_type_italic)
        self.assertEqual(2, len(node_list))
        self.assertEqual("TextNode(This, italic, None)", f"{node_list[0]}")
        self.assertEqual("TextNode( starts italic, text, None)", f"{node_list[1]}")
    
    def test_one_node_italic_at_end(self):
        node_list = split_one_node(TextNode("This ends *italic*", TextType.text_type_text), "*", TextType.text_type_italic)
        self.assertEqual(2, len(node_list))
        self.assertEqual("TextNode(This ends , text, None)", f"{node_list[0]}")
        self.assertEqual("TextNode(italic, italic, None)", f"{node_list[1]}")
    
    def test_one_node_code_at_start(self):
        node_list = split_one_node(TextNode("`This` starts as code", TextType.text_type_text), "`", TextType.text_type_code)
        self.assertEqual(2, len(node_list))
        self.assertEqual("TextNode(This, code, None)", f"{node_list[0]}")
        self.assertEqual("TextNode( starts as code, text, None)", f"{node_list[1]}")
    
    def test_one_node_code_at_end(self):
        node_list = split_one_node(TextNode("This ends as `code`", TextType.text_type_text), "`", TextType.text_type_code)
        self.assertEqual(2, len(node_list))
        self.assertEqual("TextNode(This ends as , text, None)", f"{node_list[0]}")
        self.assertEqual("TextNode(code, code, None)", f"{node_list[1]}")
    
    def test_one_node_multiple_bold_sections(self):
        node_list = split_one_node(TextNode("This **has** multiple **bold** sections", TextType.text_type_text), "**", TextType.text_type_bold)
        self.assertEqual(5, len(node_list))
        self.assertEqual("TextNode(This , text, None)", f"{node_list[0]}")
        self.assertEqual("TextNode(has, bold, None)", f"{node_list[1]}")
        self.assertEqual("TextNode( multiple , text, None)", f"{node_list[2]}")
        self.assertEqual("TextNode(bold, bold, None)", f"{node_list[3]}")
        self.assertEqual("TextNode( sections, text, None)", f"{node_list[4]}")
    
    def test_one_node_multiple_italic_sections(self):
        node_list = split_one_node(TextNode("This *has* multiple *italic* sections", TextType.text_type_text), "*", TextType.text_type_italic)
        self.assertEqual(5, len(node_list))
        self.assertEqual("TextNode(This , text, None)", f"{node_list[0]}")
        self.assertEqual("TextNode(has, italic, None)", f"{node_list[1]}")
        self.assertEqual("TextNode( multiple , text, None)", f"{node_list[2]}")
        self.assertEqual("TextNode(italic, italic, None)", f"{node_list[3]}")
        self.assertEqual("TextNode( sections, text, None)", f"{node_list[4]}")
    
    def test_one_node_multiple_code_sections(self):
        node_list = split_one_node(TextNode("This `has` multiple `code` sections", TextType.text_type_text), "`", TextType.text_type_code)
        self.assertEqual(5, len(node_list))
        self.assertEqual("TextNode(This , text, None)", f"{node_list[0]}")
        self.assertEqual("TextNode(has, code, None)", f"{node_list[1]}")
        self.assertEqual("TextNode( multiple , text, None)", f"{node_list[2]}")
        self.assertEqual("TextNode(code, code, None)", f"{node_list[3]}")
        self.assertEqual("TextNode( sections, text, None)", f"{node_list[4]}")
    
    def test_mult_nodes_bold(self):
        node1 = TextNode("This **has** some bold text", TextType.text_type_text)
        node2 = TextNode("**More bold text!**", TextType.text_type_text)
        node3 = TextNode("At end, this one is **bold**", TextType.text_type_text)
        node_list = split_nodes_delimiter([node1, node2, node3], "**", TextType.text_type_bold)
        self.assertEqual(6, len(node_list))
        self.assertEqual("TextNode(This , text, None)", f"{node_list[0]}")
        self.assertEqual("TextNode(has, bold, None)", f"{node_list[1]}")
        self.assertEqual("TextNode( some bold text, text, None)", f"{node_list[2]}")
        self.assertEqual("TextNode(More bold text!, bold, None)", f"{node_list[3]}")
        self.assertEqual("TextNode(At end, this one is , text, None)", f"{node_list[4]}")
        self.assertEqual("TextNode(bold, bold, None)", f"{node_list[5]}")