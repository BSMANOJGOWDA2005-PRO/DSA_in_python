# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
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
# Definition for singly-linked list.
#reuse the ListNode class from above
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        pre = None
        while temp is not None:
            front = temp.next
            temp.next=pre
            pre = temp#pre → 4 → 3 → 2 → 1 → None
            temp=front
        return pre