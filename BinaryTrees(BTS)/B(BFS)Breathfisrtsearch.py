#breath first search
from collections import deque#queue is used to store the nodes in the order they are visited

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

one.left=two
one.right=three
two.left=four
two.right=five
three.left=six
three.right=seven
four.left=ten
six.left=eight
seven.right=nine


def breath_search(Node):
    result = []
    queue=deque([])
    queue.append(Node)#start with the root node
    while len(queue)!=0:
        e=queue.popleft()#[1,2,3,4]it will frist ele from queue and store it in e
        result.append(e.val)
        if e.left is not None:
            queue.append(e.left)#if the left child of e is not None, add it to the queue
        if e.right is not None:
            queue.append(e.right)#if the right child of e is not None, add it to the queue
    return result

print(breath_search(one))
'''
            1
         /     \
        2       3
      /   \    / \
     4     5  6   7
    /         /     \
   10        8       9

'''