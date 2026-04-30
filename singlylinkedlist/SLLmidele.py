# Definition for singly-linked list.
n =0
temp = self.head
while temp is not None:
    temp =temp.next
    n+=1
temp = self.head
for i in range(0,n//2):
    temp = temp.next
print(temp)

#-----------------------------------------------------------------------------------
#even number linked list
n =0
temp = self.head
while temp is not None:
    temp =temp.next
    n+=1
temp = self.head
for i in range(0,n//2):
    temp = temp.next
print(temp)

#-----------------------------------------------------------------------------------
# Given the head of a singly linked list, return the middle node of the linked list.
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head 
        while fast and fast.next is not None:
            slow =slow.next
            fast= fast.next.next
        return slow
       