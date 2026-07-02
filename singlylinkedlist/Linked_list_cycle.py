class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def its_cycle(node):
    slow = node
    fast = node

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


# Create nodes
head = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)
fifth = Node(5)

# Connect nodes
head.next = second
second.next = third
third.next = fourth
fourth.next = fifth

# Create a cycle
fifth.next = third   # 5 → 3

# Check cycle
if its_cycle(head):
    print("Cycle Found")
else:
    print("No Cycle")
    
    """
    1 → 2 → 3 → 4 → 5
        ↑       ↓
        └───────┘
    """