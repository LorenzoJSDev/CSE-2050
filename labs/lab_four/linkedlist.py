"""
<linkedlist.py>

-------------------------------------------------------------
This is a script is a peice of lab four
-------------------------------------------------------------

Author: Lorenzo .S
Contributors: [" "]
Created: 02-18-2026
Last Updated: Created: 02-18-2026

"""
#=== Imports ===#
from typing import Optional, Any, Iterable

#=== Classes ===#


class Node:
    def __init__(self, item, link: Optional['Node'] = None) -> None:
        self.item = item
        self.link = link

    def __repr__(self) -> str:
        return f"Node(item:{self.item}, data: {self.link})"

class LinkedList:
    def __init__(self, items: Optional[Iterable[Any]] = None) -> None:
        self.items = items
        self._head = Node | None
        self._tail = Node | None
        self._len = 0
    
    def __len__(self) -> int:
        return self._len

    def get_head(self) -> Any | None:
        return self._head

    def get_tail(self) -> Any | None:
        return self._tail
    
    def add_last(self,item) -> None:
        pass

    def add_first(self,item) -> None:
        pass

    def remove_last(self) -> Any:
        pass

    def remove_first(self) -> Any:
        pass


