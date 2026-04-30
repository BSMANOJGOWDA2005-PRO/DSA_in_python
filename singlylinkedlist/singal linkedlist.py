# This code defines a simple linked list structure using a Node class. 
class Node:
    def __init__(self, value):
        self.value = value# Each node has a value 
        self.next = None# Each node has a reference to the next node in the list,initially its none
        
node1=Node(5)#assigning value to node1
node2=Node(10)#assigning value to node2
node3=Node(20)#assigning value to node3
node4=Node(8)#assigning value to node4

node1.next = node2#linking node1 to node2
node2.next = node3#linking node2 to node3
node3.next = node4#linking node3 to node4

print(node1.next)#output Is <__main__.Node object at 0x7f8c8c8c8c8c>
print(node1.value)#output is 5
print(node1.next.value)#output is 10
print(node1.next)#output is <__main__.Node object at 0x7f8c8c8c8c8c>


#----------------------------------------------------------------------------------
# A singly linked list is a data structure that consists of a sequence of nodes
class Nodes:
    def __init__(self,val):
        self.val=val
        self.next = None
        
class singlylinkedlist:
    def __init__(self):
        self.head=None

    def append(self,val):
        new_node=Nodes(val)
        if self.head==None:
            self.head=new_node
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next=new_node
        
    def Travers(self):
        if self.head is None:
            print("SSL is empty")
        else:
            cur = self.head
            while cur is not None:
                print(cur.val,"->",end=" ")
                cur = cur.next
            print("None")


c=singlylinkedlist()
c.append(5)
c.append(9)
c.append(15)
c.append(20)
c.Travers()
