"""

Data Structures:
    * Trees

Vocab

Node types of a Tree:
    * Root: No parents
    * Internals Nodes: Nodes with a Parent and a child
    * Leaf: Nodes with no children

Length of a path: The number of edges between two nodes
Edges: the arrows pointing between nodes

Tree Types:
    *Full Binary Tree: Each Node has at either two or 0 children
    * Complete Binary Tree: Binary tree with each level full, following left to right node pattern

Traversal Methods of a Tree from starting point:
    * Pre-Order traverse: Root -> Left -> Right
    * In-Order traverse: Left -> Root -> Right
    * Post-Order traverse: Left -> Right -> Root

Inserting Data into a binary tree:
    * Right side: Every node greater than root
    * Left side: Every node less than root

Deleting a node:
Worst case: O(n)
O(Height)
    * Leaf Node: Just set the parents side to None
    * Parent with one child Node:
    * Parent with two children Nodes: One left all the way right or One right all the way left


"""