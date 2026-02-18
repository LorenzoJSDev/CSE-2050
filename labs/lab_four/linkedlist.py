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
from typing import Optional

#=== Classes ===#


class Node:
    def __init__(self, item, link: Optional['Node'] = None) -> None:
        self.item = item
        self.link = link

    def __repr__(self) -> str:
        return f"Node(item:{self.item}, data: {self.link})"

class LinkedList:
    pass