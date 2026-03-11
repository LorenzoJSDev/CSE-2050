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
Contributors:
Created: 02-18-2026
Last Updated: Created: 02-18-2026

"""

#==== Imports ====#
from abc import ABC, abstractmethod
from dataclasses import dataclass

#-----------------------------------#

class ADT:
    """
    Docstring for moduleFour.ADT()

    Definition:
        - Class of objects whose logical behavior is defined by a set of values and operations.\
        - Logical models
        - Tells what methods the data structure will implement
        - Putting rules on data Structures

    Examples of ADTs:
        * Stack
        * Queue
        * Deque (deck)
    """
    pass

class DataStructure:
    """
    Docstring for moduleFour.DataStructure()

    Definition:
        - An implementation of ADT(logical models)
        - Concrete representations fo data

    Examples of Data Structures:
        * List
        * Linked List
        * Doubly Linked List
    """
    pass


#---- 02-18-2026 Lecture Notes ----#

#==== Abstract Datatypes ====#
class Stack(ABC):
    """ 
    Docstring for moduleFour.Stack

    Definition:
        - A list with the restriction that insertion and deletion can only be preformed from one end.
        - The end is also called the top.
        - LIFO: Last in First Out

    Stack Diagram:
    Stack = [1,2,3,4,5,6,7]
                         ^
                         Head
    Main Operations:
        * Push(item)    # TIME COMPLEXITY: O(1)
        * Pop()         # TIME COMPLEXITY: O(1)
        * Top or Peek() # TIME COMPLEXITY: O(1)
        * IsEmpty()     # TIME COMPLEXITY: O(1)
        * Len()         # TIME COMPLEXITY: O(1)
            - usually just the default __len__ function in python

    """

    def __init__(self):
        """
        Docstring for moduleFour.Stack.__init__()

        When used as a wrapper (for a list as an example) it would init self.L = []
        since it is imposing rules on the list object [] is would need to wrap around the list []
        Get it?
        """
        return

    @abstractmethod
    def push(self, item):
        """
        Docstring for moduleFour.Stack.push()

        Time complexity: O(1)
        Description:
            - Adds a new item to the stack.
            - Places a new item at the top of the stack.

        Example:
        Stack = [1,2,3,4,5,6,7]
        Stack.push(8)
        Stack = [1,2,3,4,5,6,7,8]
                               ^
                               New Head
        """
        return

    @abstractmethod
    def pop(self):
        """
        Docstring for moduleFour.Stack.pop()

        TIME COMPLEXITY: O(1)
        Description:
            - Removes and RETURNS the item at the top of the stack.
            - RETURNS the item at the top of the stack.

        Example:
        Stack = [1,2,3,4,5,6,7]
                             ^
                             Head
        Stack.pop()     #pop() removes the last item from a list by default

        Stack = [1,2,3,4,5,6]
                           ^
                           New Head
        RETURNS: 7
        """
        return

    @abstractmethod
    def peek(self):
        """
        Docstring for moduleFour.Stack.peek()

        TIME COMPLEXITY: O(1)
        Description:
            - Returns the item at the top of the stack.
            - Returns the head of the stack.
            - peek() can also be known as top()

        Example:
            Stack = [1,2,3,4,5,6,7]
            Stack.peek()    # Does not affect the stack itself.
            returns: 7
        """
        return

    @abstractmethod
    def __len__(self):
        """
        Docstring for moduleFour.Stack.__len__()

        Time complexity: O(1)
        Description:
            - Returns the number of items in the stack.
            - Can also be known as size()
        """
        return

    @abstractmethod
    def is_empty(self):
        """
        Docstring for moduleFour.Stack.isEmpty()

        Time complexity: O(1)
        Description:
            - Returns True if the stack is empty, False otherwise.
            - How this is coded depends on the data structure the stack class is wrapping around.
        """
        return

# Example of Stack Wrapper for List
class ListStack(Stack):
    """
    Docstring for moduleFour.ListStack(Stack)

    Description:
        - This is an implementation of the Stack class as a wrapper for a list object.
        - The stack class imposes rules on the list such as things can only be added and taken from the head/top of the stack/back of the list.
    """

    def __init__(self):
        """
        Docstring for moduleFour.ListStack(Stack).__init__()

        Description:
            - This implementation creates a new ListStack object.
            - Since we are wrapping the list object we need to initialize it as part of the ListStack class.
        """
        super().__init__()
        self._list = []

    def push(self, item):
        """
        Docstring for moduleFour.ListStack.push()

        Description:
            - Adds a new item to the stack.
            - Uses the append() list method since we are wrapping the list object.
        """
        self._list.append(item)

    def pop(self):
        """
        Docstring for moduleFour.ListStack.pop()

        TIME COMPLEXITY: O(1)
        Description:
            - Removes and RETURNS the item at the top of the stack.
            - raises an error it the user attempts to pop from an empty stack.
        """
        try:
            return self._list.pop()
        except IndexError:
            raise IndexError("Can not pop from empty list")

    def peek(self):
        return self._list[-1]

    def __len__(self):
        return len(self._list)

    def is_empty(self):
        return len(self._list) == 0

class Queue(ABC):
    """
    Docstring for moduleFour.Queue

    Description:
        - A list with the restriction that insertion and deletion can only be preformed from one end.
        - Insertion/Enqueue can only be preformed from the rear/end/top/head/back of the list of the list.
        - Deletion/Dequeue can only be preformed from the front/beginning of the list.
        - FIFO

    Main Operations:
        * Enqueue(Item)         # TIME COMPLEXITY: O(1)
        * Dequeue()             # TIME COMPLEXITY: O(n)
        * Peek() or Front()     # TIME COMPLEXITY: O(1)
        * IsEmpty()             # TIME COMPLEXITY: O(1)
        * Len()                 # TIME COMPLEXITY: O(1)

    Queue Diagram:
    Queue = [1,2,3,4,5,6,7]
             ^           ^
             Front       Back

    Enqueue(new element) --- > (Queue) ---> Dequeue(old element)

    Problem: Dequeue() runs in O(n), which is not good.
    """

    @abstractmethod
    def __init__(self):
        """
        Docstring for moduleFour.Queue(Queue).__init__()

        When used as a wrapper (for a list as an example) it would init self.L = []
        since it is imposing rules on the list object [] is would need to wrap around the list []
        Get it?
        """
        return

    @abstractmethod
    def enqueue(self, item):
        """
        Docstring for moduleFour.Queue.enqueue()

        TIME COMPLEXITY: O(1)
        Description:
            - Adds a new item to the back of the queue [to the back of the list].

        Example:
        Queue = [1,2,3,4,5,6,7]
                             ^
                             Back of Queue.
        Queue.enqueue(8)
        Queue = [1,2,3,4,5,6,7,8]
                                ^
                                Added 8 to the back of the queue
        """
        return

    @abstractmethod
    def dequeue(self):
        """
        Docstring for moduleFour.Queue.dequeue()

        TIME COMPLEXITY: O(n)
        Description:
            - Removes the item from the front of the queue. [from index 0 of the list, so the front of the list]
            - It runs of O(n) because once the first item is removed, all the items in the queue have to shift up one.

        Example:
        Queue = [1,2,3,4,5,6,7]
        Queue.dequeue()
        Queue = [2,3,4,5,6,7]
        RETURNS: 1
        """
        return

    @abstractmethod
    def peek(self):
        """
        Docstring for moduleFour.Queue.peek()

        TIME COMPLEXITY: O(1)
        Description:
            - Returns the item at the top of the queue without affecting the Queue.

        Example:
        Queue = [1,2,3,4,5,6,7]
        Queue.peek()
        RETURNS: 1
        """
        return

    @abstractmethod
    def __len__(self):
        """
        Docstring for moduleFour.Queue.__len__()

        TIME COMPLEXITY: O(1)
        Description:
            - Returns the number of items in the queue.
        """
        return

    @abstractmethod
    def is_empty(self):
        """
        Docstring for moduleFour.Queue.is_empty()

        TIME COMPLEXITY: O(1)
        Description:
            - Returns True if the queue is empty.
        """
        return

# Example of Queue Wrapper for List
class LazyListQueue(Queue):
    """
    Docstring for moduleFour.LazyQueue(Queue)

    Description:
        - This is an implementation of Queue as list wrapper and a more efficient/lazy .dequeue() method.
        - Modifies .dequeue() method to run in O(1) instead of O(n)
        - Dequeue now instead of actually removing element from list, it changes the head by one

    Lazy Dequeue Method Diagram:
    Queue = [1,2,3,4,5,6]
             ^
             Front
    Queue.dequeue()
    [1,2,3,4,5,6]
       ^
       New Head
    """

    def __init__(self):
        """
        Docstring for moduleFour.LazyLazyQueue(Queue)
        """
        super().__init__()
        self._head = 0 #Head variable is created to move the head instead of remove the elements.
        self._list = []
        
    def enqueue(self, item):
        """
        Docstring for moduleFour.Queue.enqueue()

        TIME COMPLEXITY: O(1)
        Description:
            - Adds a new item to the back of the queue [to the back of the list].
        """
        self._list.append(item)

    def dequeue(self):
        """
        Docstring for moduleFour.Queue.dequeue()

        TIME COMPLEXITY: O(1)
        Description:
            - Moves the head in queue in order to the item after the "removed" item creating a new head.
            - When list gets half empty, we will set the head back to 0.

        Dequeue Method Diagram:
        Queue = [1,2,3,4,5,6]
                 ^
                 Head
        Queue.dequeue()
        Queue = [1,2,3,4,5,6]
                   ^ New Head
        RETURNS: 1

        Dequeue Method Clean Up Diagram:
        Queue = [1,2,3,4,5,6,7,8]
                       ^
                       Head
        Queue.dequeue()
        Since the head is now greater than len(Queue)//2, the list is reinitialized to include only the current head element and everything after.
        Queue = [5,6,7,8]
                 ^
                 New Head
        RETURNS: 4
        """
        item = self._list[self._head]
        self._head += 1
        if self._head > len(self._list)//2:
            self._list = self._list[self._head:]
            self._head = 0
        return item

    def peek(self):
        return self._list[self._head]

    def __len__(self):
        return len(self._list) - self._head

    def is_empty(self):
        return len(self._list) - self._head == 0

class Deque(ABC):
    """
    Docstring for moduleFour.Deque

    Description:
        - Basically a stack and a queue combined.
        - Can add an remove items from both sides of the deck
        - An abstract data type that acts like a double-ended queue/ acts like both a Stack and a Queue at the same time.

    Acts both like a Stack and a Queue

    Main Operations:
        * AddFirst(item)    O(n) adds an item to the front of the deque.
        * AddLast(item)     O(1) adds an item to the back of the deque.
        * RemoveFirst(item) O(n) removes item from the front of the deque.
        * RemoveLast(item)  O(1) removes item from the back of the deque.
        * Len()             O(1) returns the length of the deque.
    """

    def __init__(self):
        """
        Docstring for moduleFour.Deque.__init__()
        """
        pass

    @abstractmethod
    def add_first(self, item):
        """
        Docstring for moduleFour.Deque.add_first()

        TIME COMPLEXITY: O(n)
        Description:
            - Adds a new item to the front of the deque.

        Example:
            Deque = [1,2,3,4,5,6,7]
            Deque.add_first(0)
            Deque = [0,1,2,3,4,5,6,7]
        """
        return

    @abstractmethod
    def add_last(self, item):
        """
        Docstring for moduleFour.Deque.add_last()

        TIME COMPLEXITY: O(1)
        Description:
            - Adds a new item to the back of the deque.

        Example:
            Deque = [1,2,3,4,5,6,7]
            Deque.add_last(8)
            Deque = [1,2,3,4,5,6,7,8]
        """
        return

    @abstractmethod
    def remove_first(self):
        """
        Docstring for moduleFour.Deque.remove_first()

        TIME COMPLEXITY: O(n)
        Description:
            - Removes the first item from the deque.

        Example:
            Deque = [1,2,3,4,5,6,7]
            Deque.remove_first()
            Deque = [2,3,4,5,6,7]
            RETURNS: 1
        """
        return

    @abstractmethod
    def remove_last(self):
        """
        Docstring for moduleFour.Deque.remove_last()

        TIME COMPLEXITY: O(1)
        Description:
            - Removes the last item from the deque.

        Example:
        Deque = [1,2,3,4,5,6,7]
        Deque.remove_last()
        Deque = [1,2,3,4,5,6]
        RETURNS: 7
        """

    def __len__(self):
        """
        Docstring for moduleFour.Deque.__len__()

        TIME COMPLEXITY: O(1)
        Description:
            - Returns the length of the deque.
        """
        return

# Example of Deque Wrapper for List
class ListDeque(Deque):
    """
    Docstring for moduleFour.ListDeque

    Description:
        - Deque implementation as a list wrapper.
    """

    def __init__(self):
        super().__init__()
        self._list =[]

    def add_first(self, item):
        self._list.append(item)

    def add_last(self, item):
        self._list.insert(0,item)

    def remove_first(self):
        return self._list.pop(0)

    def remove_last(self):
        return self._list.pop()

    def __len__(self):
        return len(self._list)

#==== Data Structures ====#

class SinglyLinkedList:
    """
    Docstring for moduleFour.SinglyLinkedList

    Description:
        - A datastructures used to create more efficient implementation of ADT Deque.
        - Storing data using a series of Node.
        - One Node points to the next node in the Series.
    Components of a SinglyLinkedList:
        * LinkedList class
        * Node class

        
    Main Operations:
        * add_last
        * add_first
        * remove_last
        * remove_first
        * len()

    SinglyLinkedList Diagram:
    SinglyLinkedList = node1(data,node2) --> node2(data,node3) ---> node3(data,None)
    !!!Note: This is not a list wrapper, these nodes are not stored within a list object!!!
        
    Problems:
        * Nodes can only access previous Nodes

    Each element is a separate object, and they will be linked like a chain
    """

    @dataclass
    class ListNode:
        """ Docstring for moduleFour.SinglyLinkedList.SinglyLinkedListNode

        Description:
            - The Node class does not have any methods, they are ment to just store and point
        """
        
        def __init__(self,data,link=None):
            """
            Docstring for moduleFour.SinglyLinkedList.SinglyLinkedListNode.__init__()
            """
            self.data = data
            self.link = link
            return

    def __init__(self):
        """
        Docstring for moduleFour.SinglyLinkedList.__init__()

        Description:
            -
        """
        self._head = None
        self._tail = None
        self._len = 0

    def add_first(self, item):
        """
        Docstring for moduleFour.SinglyLinkedList.add_first()

        Description:
            -
        """
        self._head = SinglyLinkedList.ListNode(item,self._head)
        if self._tail is None: self._tail = self._head
        self._len += 1

    def add_last(self, item):
        """
        Docstring for moduleFour.SinglyLinkedList.add_last()
        """
        if self._head is None:
            self.add_first(item)
        
        self._tail.link = SinglyLinkedList.ListNode(item)
        self._tail = self._tail.link
        self._len += 1

    def remove_first(self):
        """
        Docstring for moduleFour.SinglyLinkedList.remove_first()
        
        Returns: Node Object!
        """
        
        item = self._head
        self._head = self._head.link
        if self._head is None: self._tail = None
        self._len -= 1
        return item
        
    def remove_last(self):
        """
        Docstring for moduleFour.SinglyLinkedList.remove_last()

        Returns: Data not Node object!
        """
        if self._head is self._tail:
            return self.remove_first()
        else:
            current_node = self._head
            while current_node.link is not self._tail:
                current_node = current_node.link
            item = self._tail.data
            self._tail.link = None
            self.length -= 1
            return item
        
    def __len__(self):
        """
        Docstring for moduleFour.SinglyLinkedList.__len__()
        """
        return self._len
   
#---- 02-20-2026 Lecuture Notes ----#

class DoublyLinkedList:
    """
    Like a linked list but the nodes save both the previous node and the next node in the list

    Four Main Operations:
        * addfirst(item)    O(1) adds an item to the front of the deque
        * addlast(item)     O(1)
        * removefirst(item) O(1)
        * removelast(item)  O(1)
    """

    @dataclass
    class Node:
        def __init__(self, data, prev = None, next= None):
            self.data = data
            self.prev = prev
            self.next = next

            if prev is not None:
                self.prev.next = self
            if next is not None:
                self.next.prev = self
            return
            

    def __init__(self):
        self._head = None
        self._tail = None
        self._len = 0

    def add_first(self,value):
        if self._head is None:
            self._head = DoublyLinkedList.Node(value)
            self._tail = self._head
            self._len += 1
        else:
            self._head.prev = DoublyLinkedList.Node(value,None,self._head)
            self._head = self._head.prev
            self._len += 1
        return
    
    def add_last(self,value):
        if self._tail is None: 
            self.add_first(value)
        
        else:
            new_node = DoublyLinkedList.Node(value,self._tail,None)
            self._tail.next = new_node
            self._tail = self._tail.next
            self._len += 1
        return
    
    def remove_first(self):
        if self._head is None:
            raise IndexError("Can not remove items from an empty list")
        
        removed_node = self._head
        
        if self._head == self._tail:
            self._head = None
            self._tail = None
            self._len -= 1
        else:
            self._head = self._head.next
            self._head.prev = None
            self._len -= 1
        
        return removed_node
    
    def remove_last(self):
        if self._tail is None:
            raise IndexError("Can not remove items from an empty list")
        
        removed_node = self._tail

        if self._tail == self._head: 
            self.remove_first()
        else:
            self._tail = self._tail.prev
            self._tail.next = None
            self._len -= 1
        
        return removed_node