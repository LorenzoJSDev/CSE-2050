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
from linkedlist import Node, LinkedList
import unittest

#=== Classes ===#

class TestNode(unittest.TestCase):
    def setUp(self):
        self.node1 = Node("data")
        self.node2 = Node("2data2", self.node1)

    def test_init(self):
        self.assertEqual(self.node1.item, 'data')
        self.assertEqual(self.node1.link, None)

        
class TestLinkedList(unittest.TestCase):
    
    def setUp(self):
        self.linkedlist1 = LinkedList()


    def test_init(self):
        self.assertIs(self.linkedlist1._head, None)
        self.assertEqual(self.linkedlist1._tail, None)
        self.assertEqual(self.linkedlist1._len, 0)

if __name__ == '__main__':
    unittest.main()

