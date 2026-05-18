class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

one=Node(1)
two=Node(2)
three=Node(3)
four=Node(4)
five=Node(5)
six=Node(6)
seven=Node(7)
eight=Node(8)
nine=Node(9)
ten =Node(10)

five.left=three
five.right=four
three.left=two
three.right=nine
four.left=eight
nine.left=six
eight.left=one
nine.right=six



def preorder_traverser(node):
    if node is None:
        return

    print(node.val,end=" ")

    preorder_traverser(node.left)
    preorder_traverser(node.right)
    

preorder_traverser(five)


