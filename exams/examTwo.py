"""
Practice Question One

Stack using Python list (efficient push/pop)

Implement a Stack class using a Python list. Your implementation must support:

Methods:
    * push(x) in O(1)
    * pop() in O(1) (raise an exception if empty)
    * is_empty() in O(1) time
    * __len__() in O(1) time
"""

class Stack:

    def __init__(self):
        """
        Docstring for Stack.__init__()

        Description:
            - Initilizes Stack list wrapper object
        """
        self._list = []

    def push(self,item):
        """
        Docstring for Stack.push()
        """
        self._list.append(item)
        return
    
    def pop(self):
        """
        Docstring for Stack.pop()
        """
        return self._list.pop()
    
    def is_empty(self):
        """
        Docstring for Stack.is_empty()
        """
        return len(self._list) == 0
    
    def __len__(self):
        """
        Docstring for Stack.__len__()
        """
        return len(self._list)
    

"""
Practice Question Two

Singly linked list operations

You are given the node class:
 
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
 
 
Implement a SinglyLinkedList class with attributes head, tail, and size, supporting:

add_first(x)
remove_first()
add_last(x)
remove_last()
Notes/constraints:

Update head, tail, and size correctly.
Handle edge cases (empty list, one element).
Aim for: add_first and remove_first in O(1); add_last in O(1) (with tail); remove_last is O(n) for linked lists.

Problem Areas: remove_first(), remove_last
"""

class Node:
    
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class SinglyLinkedList:
    
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def add_first(self,item):
        self._head = Node(item)
        if self._tail is None:  self._tail = self._head
        self._size += 1

    def add_last(self,item):
        if self._head is None: 
            self.add_first(item)
        else:
            self._tail.next = Node(item)
            self._tail = self._tail.next
            self._len += 1

    def remove_first(self):
        
        if self._head is None:
            raise IndexError("Can not remove items from empty list")
        
        item = self._head
        self._head = self._head.next
        if self._head is None: self._tail = None
        self._size -= 1
        return item
    
    def remove_last(self):
        if self._tail is None:
            raise IndexError("Can not remove items from empty list")
        
        elif self._head is self._tail:
            self.remove_first()

        else: 
            current_node = self._head

            while current_node.next is not self._tail:
                current_node = current_node.next
        
            item = current_node.next
            self._tail = current_node
            self._tail.next = None
            self._len -= 1
            return item
        

    # ---------------------------------------------------- 1:00 AM Quiz 4