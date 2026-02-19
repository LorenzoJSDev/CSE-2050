"""
<test_linkedlist.py>

-------------------------------------------------------------
This is a script is a peice of lab four
-------------------------------------------------------------

Author: Lorenzo .S
Contributors: ["Jerod Abraham"]
Created: 02-18-2026
Last Updated: Created: 02-18-2026

"""

#=== Imports ===#
from linkedlist import Node, LinkedList
import unittest

#=== Classes ===#

class TestNode(unittest.TestCase):
    """
    Docstring for TestNode
    """
    def setUp(self):
        """
        Docstring for setUp
        
        :param self: Description
        """
        self.node1 = Node("data")
        self.node2 = Node("2data2", self.node1)

    def test_init_no_link(self):
        """
        Docstring for test_init_no_link
        
        :param self: Description
        """
        self.assertEqual(self.node1.item, 'data')
        self.assertIsNone(self.node1.link)

    def test_init_yes_link(self):
        """
        Docstring for test_init_yes_link
        
        :param self: Description
        """
        self.assertEqual(self.node2.item, '2data2')
        self.assertEqual(self.node2.link, self.node1)

    def test_repr_no_link(self):
        """
        Docstring for test_repr_no_link
        
        :param self: Description
        """
        expected = "Node(data)"
        self.assertEqual(repr(self.node1), expected)

    def test_repr_yes_link(self):
        """
        Docstring for test_repr_yes_link
        
        :param self: Description
        """
        expected = f"Node(2data2)"
        self.assertEqual(repr(self.node2), expected)

        
class TestLinkedList(unittest.TestCase):
    """
    Docstring for TestLinkedList
    """
    def setUp(self):
        """
        Docstring for setUp
        
        :param self: Description
        """
        self.LL1 = LinkedList()
        self.LL2 = LinkedList(['a','b','c'])
        self.LL3 = LinkedList(range(10))
        


    def test_init(self):
        """
        Docstring for test_init
        
        :param self: Description
        """
        
        # LL1 tests
        self.assertEqual(self.LL1.__len__(),0)
        self.assertIsNone(self.LL1.get_head())
        self.assertIsNone(self.LL1.get_tail())

        # LL2 tests
        self.assertEqual(self.LL2.__len__(), 3) # Get length of LL2
        self.assertEqual(self.LL2.get_head(), 'a') # Test item of _head Node in LL2
        self.assertEqual(self.LL2.get_tail(), 'c') # Test item of _tail Node in LL2

        # LL3 tests
        self.assertEqual(self.LL3.__len__(), 10) # Get length of LL3
        self.assertEqual(self.LL3.get_head(), 0) # Test item of _head Node in LL3
        self.assertEqual(self.LL3.get_tail(), 9) # Test item of _tail Node in LL3



    def test_add_last(self):
        """Docstring for test_add_last"""
        # LL1 tests
        for i in range(1, 6):
            self.LL1.add_last(i)
            self.assertEqual(len(self.LL1), i)
            self.assertEqual(self.LL1.get_head(), 1)
            self.assertEqual(self.LL1.get_tail(), i)

    def test_add_first(self):
        """ Docstring for test_add_first"""
        # LL1 tests
        for i in range(1,6):
            self.LL1.add_first(i)
            self.assertEqual(len(self.LL1),i)
            self.assertEqual(self.LL1.get_head(),i)
            self.assertEqual(self.LL1.get_tail(), 1)

    def test_remove_first(self):
        expected_values = ['a', 'b', 'c']
        original_len = len(self.LL2)

        for i in range(original_len):
            removed_node = self.LL2.remove_first()

            # remove_first now returns a Node
            self.assertEqual(removed_node, expected_values[i])

            self.assertEqual(len(self.LL2), original_len - i - 1)

            if len(self.LL2) == 0:
                self.assertIsNone(self.LL2.get_head())
                self.assertIsNone(self.LL2.get_tail())
            else:
                self.assertEqual(
                    self.LL2.get_head(),
                    expected_values[i + 1]
                )
                self.assertEqual(
                    self.LL2.get_tail(),
                    expected_values[-1]
                )

    # RuntimeError test
        with self.assertRaises(RuntimeError):
            self.LL2.remove_first()


    def test_remove_last(self):
        expected_values = ['a', 'b', 'c']
        original_len = len(self.LL2)

        for i in range(original_len):
            removed_node = self.LL2.remove_last()

            # remove_last now returns a Node
            self.assertEqual(
                removed_node,
                expected_values[original_len - 1 - i]
            )

            self.assertEqual(len(self.LL2), original_len - i - 1)

            if len(self.LL2) == 0:
                self.assertIsNone(self.LL2.get_head())
                self.assertIsNone(self.LL2.get_tail())
            else:
                self.assertEqual(
                    self.LL2.get_head(),
                    expected_values[0]
                )
                self.assertEqual(
                    self.LL2.get_tail(),
                    expected_values[original_len - 2 - i]
                )

        # RuntimeError test
        with self.assertRaises(RuntimeError):
            self.LL2.remove_last()

 


if __name__ == '__main__':
    unittest.main()

