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

class Node:
    def __init__(self, item, link: Node = None) -> None:
        self.this = item
        self.link = link

    def __repr__(self) -> str:
        return f"{self.item},{self.link}"

class LinkedList:
    pass