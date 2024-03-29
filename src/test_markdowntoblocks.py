import unittest

from htmlnode import markdown_to_blocks

class TestMarkdownToBlocks(unittest.TestCase):
    def test_bootdev_example(self):
        markdown = """This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items"""
        expected_blocks = [
            'This is **bolded** paragraph', 
            'This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line', 
            '* This is a list\n* with items'
        ]
        self.assertEqual(expected_blocks, markdown_to_blocks(markdown))
    
    def test_bootdev_with_extra_whitespace(self):
        markdown = """This is **bolded** paragraph          
        

            This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line





* This is a list
* with items"""
        expected_blocks = [
            'This is **bolded** paragraph', 
            'This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line', 
            '* This is a list\n* with items'
        ]
        self.assertEqual(expected_blocks, markdown_to_blocks(markdown))