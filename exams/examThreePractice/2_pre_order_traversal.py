"""
Author: Lorenzo .S
Date: 4/14/2026

Notes:
    None
"""
"""
Implement the preorder(self) method so that 
it generates the nodes of the tree in 
pre-order traversal.

In pre-order traversal:

Visit the current node first
Then recursively visit each child from left to right
"""


class TreeNode:
    def __init__(self, parent, data):
        self.parent = parent
        self.data = data
        self.children = []

    def add_child(self, data):
        child = TreeNode(self, data)
        self.children.append(child)
        return child

    def preorder(self):
        result = []
        result.append(self.data)
        for child in self.children:
            result.extend(child.preorder())
        return result

A = TreeNode(None,"A")
B = TreeNode(A,"B")
A.children.append(B)
C = TreeNode(A,"C")
A.children.append(C)
D = TreeNode(B,"D")
B.children.append(D)

print(A.preorder())