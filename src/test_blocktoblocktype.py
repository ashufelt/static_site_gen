import unittest

from htmlnode import BlockType, block_to_block_type

class TestBlockToBLockType(unittest.TestCase):

    #### Heading tests ####
    def test_heading_1(self):
        text = "# heading "
        self.assertEqual(BlockType.heading, block_to_block_type(text))
    
    def test_heading_2(self):
        text = "## heading"
        self.assertEqual(BlockType.heading, block_to_block_type(text))
    
    def test_heading_3(self):
        text = "### heading"
        self.assertEqual(BlockType.heading, block_to_block_type(text))
    
    def test_heading_4(self):
        text = "#### heading"
        self.assertEqual(BlockType.heading, block_to_block_type(text))
    
    def test_heading_5(self):
        text = "##### heading"
        self.assertEqual(BlockType.heading, block_to_block_type(text))

    def test_heading_6(self):
        text = "###### heading"
        self.assertEqual(BlockType.heading, block_to_block_type(text))
    
    def test_paragraph_looks_like_heading(self):
        text = "##not a heading"
        self.assertEqual(BlockType.paragraph, block_to_block_type(text))
    
    def test_paragraph_from_empty_heading(self):
        text = "###     "
        self.assertEqual(BlockType.paragraph, block_to_block_type(text))
    
    def test_paragraph_heading_with_7(self):
        text = "####### not a heading"
        self.assertEqual(BlockType.paragraph, block_to_block_type(text))
    
    def test_paragraph_heading_with_space_before(self):
        text = " ### not a heading"
        self.assertEqual(BlockType.paragraph, block_to_block_type(text))
    
    #### Code block testing ####
    def test_code_block_one_line(self):
        text = "``` code block ```"
        self.assertEqual(BlockType.code, block_to_block_type(text))
    
    def test_code_block_multi_line(self):
        text = """```
        code block
        on multiple
        lines
        ```"""
        self.assertEqual(BlockType.code, block_to_block_type(text))
    
    def test_empty_code_block(self):
        text = "``````"
        self.assertEqual(BlockType.code, block_to_block_type(text))
    
    def test_paragraph_code_block_without_closing_marks(self):
        text = "``` This code block doesn't close properly ``"
        self.assertEqual(BlockType.paragraph, block_to_block_type(text))
    
    #### Quote block testing ####
    def test_quote_block_one_line(self):
        text = ">one line quote block"
        self.assertEqual(BlockType.quote, block_to_block_type(text))
    
    def test_quote_block_three_lines(self):
        text = """>one line
>two lines 
>three lines"""
        self.assertEqual(BlockType.quote, block_to_block_type(text))
    
    def test_paragraph_quote_missing_middle_mark(self):
        text = """>one line
two lines 
>three lines"""
        self.assertEqual(BlockType.paragraph, block_to_block_type(text))
    
    #### Unordered list testing ####
    def test_u_list_one_line_star(self):
        text = "* one bullet point"
        self.assertEqual(BlockType.u_list, block_to_block_type(text))
    
    def test_u_list_one_line_dash(self):
        text = "- one bullet point"
        self.assertEqual(BlockType.u_list, block_to_block_type(text))

    def test_u_list_multiple_line_star(self):
        text = """* one bullet point
* two bullet points
* three"""
        self.assertEqual(BlockType.u_list, block_to_block_type(text))
    
    def test_u_list_multiple_line_dash(self):
        text = """- one bullet point
- two bullet points
- three"""
        self.assertEqual(BlockType.u_list, block_to_block_type(text))
    
    #### Ordered list testing ####
    def test_o_list_one_line(self):
        text = "1. First line"
        self.assertEqual(BlockType.o_list, block_to_block_type(text))
    
    def test_o_list_multiple_lines(self):
        text = """1. first
2. second
3. third
4. fourth
5. fifth"""
        self.assertEqual(BlockType.o_list, block_to_block_type(text))