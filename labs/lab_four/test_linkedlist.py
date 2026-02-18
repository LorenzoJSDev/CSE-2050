"""
<test_linkedlist.py>

-------------------------------------------------------------
This is a script is a piece of lab four
-------------------------------------------------------------

Author: Lorenzo .S
Contributors: [" "]
Created: 02-18-2026
Last Updated: Created: 02-18-2026

"""

#=== Imports ===#

import unittest
from unittest import TestCase
from linkedlist import Node, LinkedList

#=== Classes ===#

class TestNode(TestCase):
    def setUp(self):
        self.node1 = Node("data")
        self.node2 = Node("2data2", self.node1)

    def test_init_no_link(self):
        self.assertEqual(self.node1.item, 'data')
        self.assertIsNone(self.node1.link)

    def test_init_yes_link(self):
        self.assertEqual(self.node2.item, '2data2')
        self.assertEqual(self.node2.link, self.node1)

    def test_repr_no_link(self):
        expected = "Node(item:data, data: None)"
        self.assertEqual(repr(self.node1), expected)

    def test_repr_yes_link(self):
        expected = f"Node(item:2data2, data: {repr(self.node1)})"
        self.assertEqual(repr(self.node2), expected)

    # self.assertEqual(self.a1.name, 'Arthur')

if __name__ == "__main__":
    unittest.main()
