class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.pre= None
        
#insert at the beginning of the list
class Double_linkedlist:
    def __init__(self):
        self.head = None
        
    def insert_values(self,val):
        new_node = Node(val)
        if self.head is None:
            self.head=new_node
        else:
            new_node.next=self.head
            self.head.pre=new_node
            self.head=new_node
    
#------------------------------------------------------------------------------------         

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.pre= None
        
#append at the beginning of the list
class Double_linkedlist:
    def __init__(self):
        self.head = None        
    def append(self,val):
        new_node= Node(val)
        if self.head is None:
            self.head = new_node
        else:
            curr =self.head
            while curr.next is not None:
                cur = curr.next
            curr.next = new_node
            new_node.pre=curr
            


    

    