#Binary Tree Inorder Traversal
def inorder_traverser(node):
    if node is None:
        return

    inorder_traverser(node.left)
    print(node.val,end=" ")
    inorder_traverser(node.right)

inorder_traverser("five")

#----------------------------------------------------------
#Binary Tree Postorder Traversal
def postorder_traverser(node):
    if node is None:
        return

    postorder_traverser(node.left)
    postorder_traverser(node.right)
    print(node.val,end=" ")

postorder_traverser(five)

