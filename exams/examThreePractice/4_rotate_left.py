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

            if parent:
                if self is parent.left
                    pass