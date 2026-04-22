"""
Author: Lorenzo .S
Date: 4/14/2026


Notes:
    Wasn't even able to put a line of code down this question was so annoying
"""

"""
Implement the postorder(self) method so that it generates the nodes of the tree in post-order traversal.

In post-order traversal: Recursively visit each child from left to right
Visit the current node last
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

    def postorder(self):
        # Left -> Right -> Node
        result = []
        for child in self.children:
            result.extend(child.postorder())
        result.append(self.data)
        return result

A = TreeNode(None,"A")
B = TreeNode(A,"B")
A.children.append(B)
C = TreeNode(A,"C")
A.children.append(C)
D = TreeNode(B,"D")
B.children.append(D)

print(A.postorder())

"""
Solution:

def postorder(self):
    result = []

    for child in self.children:
        result.extend(child.postorder())

    result.append(self.data)

    return result
"""

