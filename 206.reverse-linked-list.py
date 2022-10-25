# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        ## append the values in a stack, then pop the values and create a new list ezpz

        dummy = ListNode(-1)
        dummy.next = head

        stack = list()

        while dummy.next:
            stack.append(dummy.next.val)
            dummy = dummy.next

        temp = new_head = ListNode(-1)

        while stack:
            node = ListNode(stack.pop())
            temp.next = node
            temp = temp.next

        return new_head.next
