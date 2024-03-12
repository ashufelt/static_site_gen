import unittest

from htmlnode import ParentNode, LeafNode

class TestParentNode(unittest.TestCase):
    def test_one_child_no_parent_props(self):
        leaf = LeafNode("p", "Leaf node")
        parent = ParentNode("h1", [leaf])
        self.assertEqual("<h1><p>Leaf node</p></h1>", parent.to_html())
    
    def test_one_child_with_parent_props(self):
        leaf = LeafNode("p", "Leaf node")
        parent = ParentNode("h1", [leaf], {"style":"bold"})
        self.assertEqual("<h1 style=bold><p>Leaf node</p></h1>", parent.to_html())
    
    def test_multiple_children(self):
        leaf = LeafNode("p", "Leaf node 1")
        leaf2 = LeafNode("p", "Leaf node 2")
        parent = ParentNode("h1", [leaf, leaf2], {"style":"bold"})
        self.assertEqual("<h1 style=bold><p>Leaf node 1</p><p>Leaf node 2</p></h1>", parent.to_html())
    
    def test_parent_to_parent_to_leaf(self):
        leaf = LeafNode("p", "Leaf node")
        inner_parent = ParentNode("h1", [leaf], {"style":"bold"})
        top_parent = ParentNode("body", [inner_parent])
        self.assertEqual("<body><h1 style=bold><p>Leaf node</p></h1></body>", top_parent.to_html())
    
    def test_mixed_leafs_and_nested_parents(self):
        leaf = LeafNode("p", "Leaf node 1")
        leaf2 = LeafNode("p", "Leaf node 2")
        inner_parent1_2 = ParentNode("h2", [leaf2], {"style":"bold"})
        inner_parent1 = ParentNode("h1", [inner_parent1_2], {"style":"bold"})
        leaf3 = LeafNode("p", "Leaf node 3", {"style":"italic"})
        leaf4 = LeafNode("p", "Leaf node 4")
        leaf5 = LeafNode("p", "Leaf node 5")
        inner_parent2 = ParentNode("h1", [leaf4, leaf5])
        top_parent = ParentNode("body", [leaf, inner_parent1, leaf3, inner_parent2])
        expected = "<body><p>Leaf node 1</p><h1 style=bold><h2 style=bold><p>Leaf node 2</p></h2></h1><p style=italic>Leaf node 3</p><h1><p>Leaf node 4</p><p>Leaf node 5</p></h1></body>"
        self.assertEqual(expected, top_parent.to_html())
        
