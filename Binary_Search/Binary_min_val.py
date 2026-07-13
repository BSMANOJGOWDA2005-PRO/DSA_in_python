class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# Create the tree manually
root = Node(8)
root.left = Node(3)
root.right = Node(10)
root.left.left = Node(1)
root.left.right = Node(6)


def mini_value(root):
    temp = root
    while temp is not None and temp.left is not None:
        temp = temp.left
    return temp.val


print(mini_value(root))#Output: 1
'''
        8
       / \
      3   10
     / \
    1   6
'''
    