import unittest

from main import extract_markdown_links, extract_markdown_images

class TestExtractMarkdown(unittest.TestCase):
    def test_one_image_simple(self):
        images = extract_markdown_images("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)")
        self.assertEqual([('image', 'https://i.imgur.com/zjjcJKZ.png')], images)
    
    def test_two_images_simple(self):
        images = extract_markdown_images("This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and ![another](https://i.imgur.com/dfsdkjfd.png)")
        self.assertEqual([("image", "https://i.imgur.com/zjjcJKZ.png"), ("another", "https://i.imgur.com/dfsdkjfd.png")], images)