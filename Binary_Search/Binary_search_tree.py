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

# Value to search
val = 6

temp = root

while temp:
    if temp.val == val:
        print("Found:", temp.val)
        break
    elif val < temp.val:
        temp = temp.left
    else:
        temp = temp.right

if temp is None:
    print("Not Found")
    

'''
      8
     / \
    3   10
   / \
  1   6
  
'''
#output:Found: 6
#TC:O(n) where h is the height of the tree