import unittest

from htmlnode import ParentNode, LeafNode, block_to_html_node

class TestBlockToHTMLNode(unittest.TestCase):
    def test_one_line_paragraph(self):
        text = "This is a one line paragraph"
        node = block_to_html_node(text)
        expected = LeafNode("p", "This is a one line paragraph", None)
        self.assertEqual(f"{expected}", f"{node}")
    
    def test_two_line_paragraph(self):
        text = """This is a 
two line paragraph"""
        node = block_to_html_node(text)
        expected = LeafNode("p", "This is a \ntwo line paragraph", None)
        self.assertEqual(f"{expected}", f"{node}")
    
    def test_paragraph_with_extra_whitespace(self):
        text = "      This paragraph should have the whitespace removed at beginning and end         "
        node = block_to_html_node(text)
        expected = LeafNode("p", "This paragraph should have the whitespace removed at beginning and end", None)
        self.assertEqual(f"{expected}", f"{node}")
    
    def test_heading_level_1(self):
        text = "# heading"
        node = block_to_html_node(text)
        expected = LeafNode("h1", "heading", None)
        self.assertEqual(f"{expected}", f"{node}")
    
    def test_heading_level_2(self):
        text = "## heading"
        node = block_to_html_node(text)
        expected = LeafNode("h2", "heading", None)
        self.assertEqual(f"{expected}", f"{node}")
    
    def test_heading_level_4(self):
        text = "#### heading"
        node = block_to_html_node(text)
        expected = LeafNode("h4", "heading", None)
        self.assertEqual(f"{expected}", f"{node}")
    
    def test_heading_level_6(self):
        text = "###### heading"
        node = block_to_html_node(text)
        expected = LeafNode("h6", "heading", None)
        self.assertEqual(f"{expected}", f"{node}")
    
    def test_heading_extra_whitespace(self):
        text = "## heading                "
        node = block_to_html_node(text)
        expected = LeafNode("h2", "heading", None)
        self.assertEqual(f"{expected}", f"{node}")
    
    def test_code_one_line(self):
        text = "``` code block ```"
        node = block_to_html_node(text)
        expected_inner = LeafNode("code", "code block", None)
        expected_outer = ParentNode("pre", [expected_inner], None)
        self.assertEqual(f"{expected_outer}", f"{node}")
    
    def test_code_multiple_lines(self):
        text = """```
code block with multiple lines
more lines
even more lines
```
"""
        node = block_to_html_node(text)
        expected_inner = LeafNode("code", "code block with multiple lines\nmore lines\neven more lines", None)
        expected_outer = ParentNode("pre", [expected_inner], None)
        self.assertEqual(f"{expected_outer}", f"{node}")
    
    def test_quote_one_line(self):
        text = ">  one line of quote"
        node = block_to_html_node(text)
        expected = LeafNode("blockquote", "one line of quote", None)
        self.assertEqual(f"{expected}", f"{node}")
    
    def test_quote_two_lines(self):
        text = """>first line   
>   2nd line"""
        node = block_to_html_node(text)
        expected = LeafNode("blockquote", "first line\n2nd line", None)
        self.assertEqual(f"{expected}", f"{node}")
    
    def test_ulist_one_entry(self):
        text = """* first entry of list"""
        node = block_to_html_node(text)
        expected_list_items = [
            LeafNode("li", "first entry of list", None)
        ]
        expected = ParentNode("ul", expected_list_items, None)
        self.assertEqual(f"{expected}", f"{node}")
    
    def test_ulist_many_entries(self):
        text = """* first
* second
* third
- fourth
- fifth"""
        node = block_to_html_node(text)
        expected_list_items = [
            LeafNode("li", "first", None),
            LeafNode("li", "second", None),
            LeafNode("li", "third", None),
            LeafNode("li", "fourth", None),
            LeafNode("li", "fifth", None)
        ]
        expected = ParentNode("ul", expected_list_items, None)
        self.assertEqual(f"{expected}", f"{node}")
    
    def test_olist_one_entry(self):
        text = """1. first entry of list"""
        node = block_to_html_node(text)
        expected_list_items = [
            LeafNode("li", "first entry of list", None)
        ]
        expected = ParentNode("ol", expected_list_items, None)
        self.assertEqual(f"{expected}", f"{node}")
    
    def test_olist_many_entries(self):
        text = """1. first
2. second
3. third
4. fourth
5. fifth"""
        node = block_to_html_node(text)
        expected_list_items = [
            LeafNode("li", "first", None),
            LeafNode("li", "second", None),
            LeafNode("li", "third", None),
            LeafNode("li", "fourth", None),
            LeafNode("li", "fifth", None)
        ]
        expected = ParentNode("ol", expected_list_items, None)
        self.assertEqual(f"{expected}", f"{node}")