"""
<moduleFour.py>

-------------------------------------------------------------
Notes for CSE 2050 module four which covers:

- Abstract Data Types
    * Stack
    * Queue
    * Deque (deck)

- Data Structure
    * List
    * Linked list
    * Doubly Linked List

-------------------------------------------------------------

Author: Lorenzo .S
Contributors: [" "]
Created: 02-18-2026
Last Updated: Created: 02-18-2026

"""


#---- 02-18-2026 Lecuture Notes ----#

class Stack:
    """ 
    TBD
    """
    pass

# You take a data structure like a list, and modify it so it only has the fucntionality you want it to

class Queue:
    """
    Definition:

    Main operations:
        * enqueue
        * dequeue

    Problem: dequeue runs in O(n), which is not good.
    """
    def __init__(self):
        self._L = []
 
    def enqueue(self, item):
        self._L.append(item)
 
    def dequeue(self):
        return self._L.pop(0)
 
    def peek(self):
        return self._L[0]
 
    def __len__(self):
        return len(self._L)
 
    def isempty(self):
        return len(self) == 0


class LazyQueue(Queue):
    """
    Docstring for ListQueueFakeDelete

    Defintion: 
    A subclass of Queue that implement lazy dequeue
    modifies the dequeue function in order to run in O(1) not O(n)
    """

    def __init__(self):
        super().__init__()
        self._head = 0 #Head variable is created to move the head instead of remove the element
        
    
    def dequeue(self):
        item = self.peek()
        self._head += 1
        return item

    def peek(self):
        return self._L[self._head]

    def __len__(self):
        return len(self._L) - self._head
    
    """
    Takes less time for delete since it doesnt have to go to the begining of the list
    """

class Deque(Stack and Queue):
    """
    Docstring for Deque

    Defintion: An abstract data type that acts like a double-ended queue/ acts like both a Stack and a Queue at the same time.

    Acts both like a Stack and a Queue

    Main Operations:
        * addfirst(item)    O(n) adds an item to the front of the deque
        * addlast(item)     O(1)
        * removefirst(item) O(n)
        * removelast(item)  O(1)
        * len   
    """

    pass

class LinkedList:
    """
    Docstring for LinkedList

    Definition: a structure we will use to create a more efficient implimentaion of the ADT deque

    Components of a LinkedList:
        * Node:

        
    Problems:

    Nodes can only access prevoius Nodes
    """

    class Node:
        """
        Docstring for Node

        Each Node points to the previous Node in the linked list
        """

        def __init__(self,data,link=None):
            self.data = data
            self.link = link
            return

    class LinkedList:
        
        def __init__(self):
            self._head = None

        def addfirst(self,item):
            self._head = LinkedList.Node(item,self._head)
            return

    
