import unittest

from htmlnode import HTMLNode, block_to_html_node

class TestBlockToHTMLNode(unittest.TestCase):
    def test_one_line_paragraph(self):
        text = "This is a one line paragraph"
        node = block_to_html_node(text)
        expected = HTMLNode("p", "This is a one line paragraph", None, None)
        self.assertEqual(f"{expected}", f"{node}")
    
    def test_two_line_paragraph(self):
        text = """This is a 
two line paragraph"""
        node = block_to_html_node(text)
        expected = HTMLNode("p", "This is a \ntwo line paragraph", None, None)
        self.assertEqual(f"{expected}", f"{node}")
    
    def test_paragraph_with_extra_whitespace(self):
        text = "      This paragraph should have the whitespace removed at beginning and end         "
        node = block_to_html_node(text)
        expected = HTMLNode("p", "This paragraph should have the whitespace removed at beginning and end", None, None)
        self.assertEqual(f"{expected}", f"{node}")
    
    def test_heading_level_1(self):
        text = "# heading"
        node = block_to_html_node(text)
        expected = HTMLNode("h1", "heading", None, None)
        self.assertEqual(f"{expected}", f"{node}")
    
    def test_heading_level_2(self):
        text = "## heading"
        node = block_to_html_node(text)
        expected = HTMLNode("h2", "heading", None, None)
        self.assertEqual(f"{expected}", f"{node}")
    
    def test_heading_level_4(self):
        text = "#### heading"
        node = block_to_html_node(text)
        expected = HTMLNode("h4", "heading", None, None)
        self.assertEqual(f"{expected}", f"{node}")
    
    def test_heading_level_6(self):
        text = "###### heading"
        node = block_to_html_node(text)
        expected = HTMLNode("h6", "heading", None, None)
        self.assertEqual(f"{expected}", f"{node}")
    
    def test_heading_extra_whitespace(self):
        text = "## heading                "
        node = block_to_html_node(text)
        expected = HTMLNode("h2", "heading", None, None)
        self.assertEqual(f"{expected}", f"{node}")
    
    def test_code_one_line(self):
        text = "``` code block ```"
        node = block_to_html_node(text)
        expected_inner = HTMLNode("code", "code block", None, None)
        expected_outer = HTMLNode("pre", None, [expected_inner], None)
        self.assertEqual(f"{expected_outer}", f"{node}")
    
    def test_code_multiple_lines(self):
        text = """```
code block with multiple lines
more lines
even more lines
```
"""
        node = block_to_html_node(text)
        expected_inner = HTMLNode("code", "code block with multiple lines\nmore lines\neven more lines", None, None)
        expected_outer = HTMLNode("pre", None, [expected_inner], None)
        self.assertEqual(f"{expected_outer}", f"{node}")
    
    def test_quote_one_line(self):
        text = ">  one line of quote"
        node = block_to_html_node(text)
        expected = HTMLNode("blockquote", "one line of quote", None, None)
        self.assertEqual(f"{expected}", f"{node}")
    
    def test_quote_two_lines(self):
        text = """>first line   
>   2nd line"""
        node = block_to_html_node(text)
        expected = HTMLNode("blockquote", "first line\n2nd line", None, None)
        self.assertEqual(f"{expected}", f"{node}")
    
    def test_ulist_one_entry(self):
        text = """* first entry of list"""
        node = block_to_html_node(text)
        expected_list_items = [
            HTMLNode("li", "first entry of list", None, None)
        ]
        expected = HTMLNode("ul", None, expected_list_items, None)
        self.assertEqual(f"{expected}", f"{node}")
    
    def test_ulist_many_entries(self):
        text = """* first
* second
* third
- fourth
- fifth"""
        node = block_to_html_node(text)
        expected_list_items = [
            HTMLNode("li", "first", None, None),
            HTMLNode("li", "second", None, None),
            HTMLNode("li", "third", None, None),
            HTMLNode("li", "fourth", None, None),
            HTMLNode("li", "fifth", None, None)
        ]
        expected = HTMLNode("ul", None, expected_list_items, None)
        self.assertEqual(f"{expected}", f"{node}")
    
    def test_olist_one_entry(self):
        text = """1. first entry of list"""
        node = block_to_html_node(text)
        expected_list_items = [
            HTMLNode("li", "first entry of list", None, None)
        ]
        expected = HTMLNode("ol", None, expected_list_items, None)
        self.assertEqual(f"{expected}", f"{node}")
    
    def test_olist_many_entries(self):
        text = """1. first
2. second
3. third
4. fourth
5. fifth"""
        node = block_to_html_node(text)
        expected_list_items = [
            HTMLNode("li", "first", None, None),
            HTMLNode("li", "second", None, None),
            HTMLNode("li", "third", None, None),
            HTMLNode("li", "fourth", None, None),
            HTMLNode("li", "fifth", None, None)
        ]
        expected = HTMLNode("ol", None, expected_list_items, None)
        self.assertEqual(f"{expected}", f"{node}")