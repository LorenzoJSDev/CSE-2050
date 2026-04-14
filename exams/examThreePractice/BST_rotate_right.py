"""
Author: Lorenzo .S
Date: 4/13/2026


Notes:
    None
"""




"""
Implement the rotate_right(self, parent) method.

Your method should:

perform a right rotation,
update the weights of the affected nodes,
reconnect the rotated subtree to the parent if parent is not None,
return the new root of the rotated subtree.
"""


class PartiallyBalancedBSTNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.weight = 1

    def update_weight(self):
        left_w = self.left.weight if self.left else 0
        right_w = self.right.weight if self.right else 0
        self.weight = left_w + right_w + 1
        return left_w, right_w

    def rotate_right(self, parent):
        new_subtree_root = self.left
        if parent:
            if parent.left is self:
                parent.left = new_subtree_root
            else:
                parent.right = new_subtree_root
            parent.update_weight()
        old_right = new_subtree_root.right
        self.left = None
        new_subtree_root.right = self
        self.left = old_right
        self.update_weight()
        new_subtree_root.update_weight()
        return new_subtree_root
