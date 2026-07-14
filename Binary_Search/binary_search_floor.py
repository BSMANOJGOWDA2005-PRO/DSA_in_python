class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# Create BST
root = Node(8)
root.left = Node(3)
root.right = Node(10)

root.left.left = Node(1)
root.left.right = Node(6)

root.left.right.left = Node(4)
root.left.right.right = Node(7)

root.right.right = Node(14)
root.right.right.left = Node(13)


# Find Floor
def find_floor(root, inp):
    floor = -1

    while root is not None:
        if root.val == inp:
            return root.val
        elif root.val < inp:
            floor = root.val
            root = root.right
        else:
            root = root.left

    return floor


inp = 12
print("Floor:", find_floor(root, inp))

'''
            8
          /   \
         3     10
        / \      \
       1   6      14
          / \     /
         4   7   13
'''
