"""
Author: Lorenzo .S
Date: 4/13/2026


Notes:
    None
"""


"""
Implement the rotate_left(self, parent) method.

Your method should:

perform a left rotation,
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

    def rotate_left(self, parent):
        if self.right:
            new_subtree_root = self.right

        #If Parent
            if parent:
                if parent.right == self:
                    parent.right = new_subtree_root
                else:
                    parent.left = new_subtree_root
                parent.update_weight()

        #If new_subtree_root had left child node
            if new_subtree_root.left:
                old_subtree_root_left = new_subtree_root.left
                self.right = old_subtree_root_left
                old_subtree_root_left.update_weight()
            else:
                self.right = None

            new_subtree_root.left = self
            self.update_weight()
            new_subtree_root.update_weight()
            return new_subtree_root

        #If self does not have a right node
        else:
            return self