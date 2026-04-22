"""
Author: Lorenzo .S
Date: 4/14/2026


Notes:
    None
"""


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
        # TODO: Implement this method
        pass
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
        #Check to see if left rotation is possible
        if self.right:
            new_subtree_root = self.right

            #Check to see if parent
            if parent:
                if self == parent.right:
                    parent.right = new_subtree_root
                else:
                    parent.left = new_subtree_root
                parent.update_weight()

            #Continue
            if new_subtree_root.left:
                old_subtree_left = new_subtree_root.left
                new_subtree_root.left = self
                self.right = old_subtree_left
            else:
                self.right = None
                new_subtree_root.left = self

            self.update_weight()
            new_subtree_root.update_weight()
            return new_subtree_root

        else:
            return self






