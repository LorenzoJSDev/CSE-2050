"""
<linkedlist.py>

-------------------------------------------------------------
This is a script is a peice of lab four
-------------------------------------------------------------

Author: Lorenzo .S
Contributors: ["Jerod Abraham"]
Created: 02-18-2026
Last Updated: Created: 02-18-2026

"""
#=== Imports ===#
from typing import Optional, Any, Iterable

#=== Classes ===#


class Node:
    """
    Docstring for Node
    """
    def __init__(self, item, link: Optional['Node'] = None) -> None:
        """
        Docstring for __init__
        
        :param self: Description
        :param item: Description
        :param link: Description
        :type link: Optional['Node']
        """
        self.item = item
        self.link = link

    def __repr__(self) -> str:
        """
        Docstring for __repr__
        
        :param self: Description
        :return: Description
        :rtype: str
        """
        return f"Node(item:{self.item}, data: {self.link})"

class LinkedList:
    """
    Docstring for LinkedList
    """
    def __init__(self, items: Optional[Iterable[Any]] = None) -> None:
        """
        Docstring for __init__
        
        :param self: Description
        :param items: Description
        :type items: Optional[Iterable[Any]]
        """
        self._head = None
        self._tail = None 
        self._len = 0

        if items is not None: 
            for item in items: 
                self.add_last(item)
        else:
            self.items = None

        return
    
    def __len__(self) -> int:
        """
        Docstring for __len__
        
        :param self: Description
        :return: Description
        :rtype: int
        """
        return self._len

    def get_head(self) -> Any | None:
        """
        Docstring for get_head
        
        :param self: Description
        :return: Description
        :rtype: Any | None
        """
        return self._head

    def get_tail(self) -> Any | None:
        """
        Docstring for get_tail
        
        :param self: Description
        :return: Description
        :rtype: Any | None
        """
        return self._tail
    
    def add_first(self,item) -> None:
        """
        Docstring for add_first
        
        :param self: Description
        :param item: Description
        """
        self._head = Node(item, self._head)
        if self._tail is None: 
            self._tail = self._head
        self._len += 1

    
    def add_last(self,item) -> None:
        """
        Docstring for add_last
        
        :param self: Description
        :param item: Description
        """
        if self._head is None:
            self.add_first(item)
        else:
            self._tail.link = Node(item)
            self._tail = self._tail.link
            self._len += 1


    def remove_first(self) -> Any:
        """
        Docstring for remove_first
        
        :param self: Description
        :return: Description
        :rtype: Any
        """
        if self._head is None:
            raise RuntimeError("Cannot remove_first from an empty LinkedList")

        item = self._head.item
        self._head = self._head.link

        if self._head is None:
            self._tail = None

        self._len -= 1
        return item


    def remove_last(self) -> Any:
        """
        Docstring for remove_last
        
        :param self: Description
        :return: Description
        :rtype: Any
        """
        if self._head is None:
            raise RuntimeError("Cannot remove_last from an empty LinkedList")
        if self._head is self._tail:
            return self.remove_first()
        currentnode = self._head
        while currentnode.link is not self._tail:
            currentnode = currentnode.link
        item = self._tail.item
        self._tail = currentnode
        self._tail.link = None
        self._len -= 1
        return item


   


