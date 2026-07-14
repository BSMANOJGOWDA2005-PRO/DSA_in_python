class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# Create BST
root = Node(9)
root.left = Node(3)
root.right = Node(12)

root.left.left = Node(2)
root.left.right = Node(7)

root.left.right.left = Node(4)
root.left.right.right = Node(9)

root.right.right = Node(15)
root.right.right.left = Node(14)


# Find Ceil
def find_ceil(root, inp):
    ceil = -1

    while root:
        if root.val == inp:
            return root.val
        elif inp > root.val:
            root = root.right
        else:
            ceil = root.val
            root = root.left

    return ceil


inp = 13
print("Ceil:", find_ceil(root, inp))#output: 14

"""
            9
          /   \
         3     12
        / \      \
       2   7     15
          / \     /
         4   9  14
"""
