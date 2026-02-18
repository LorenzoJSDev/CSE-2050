"""
<test_linkedlist.py>

-------------------------------------------------------------
This is a script is a peice of lab four
-------------------------------------------------------------

Author: Lorenzo .S
Contributors: [" "]
Created: 02-18-2026
Last Updated: Created: 02-18-2026

"""

#=== Imports ===#

from unittest import TestCase
from linkedlist import Node, LinkedList

#=== Classes ===#

class TestNode(TestCase):
    def setup(self):
        self.node1 = Node("data")
        self.node2 = Node("2data2", self.node1)

    def test_init(self):
        self.assertEqual(self.node1.item, 'data')
        self.assertEqual(self.node1.item, None)

    # self.assertEqual(self.a1.name, 'Arthur')
