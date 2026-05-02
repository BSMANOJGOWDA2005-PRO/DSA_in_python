# Definition for doubly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None, prev=None):
#         self.val = val
#         self.next = next
#         self.prev = prev
from typing import Optional

from ex import ListNode
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        stack = []
        while temp is not None:
            stack.append(temp.val)
            temp = temp.next
        temp = head
        while temp is not None:
            e = stack.pop()
            temp.val=e
            temp =temp.next
        return head
#--------------------------------------------------------
#doubly linked list
def reverse(self,val):
    if head.next is None:
        return head
    temp =0
    pre =None
    while temp is not None:
        front = temp.next
        temp.next = pre
        temp.pre=front
        pre = temp 
        temp = front
    return pre