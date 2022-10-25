# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        ## the idea that comes to mind is traverse the list with teo pointers

        dummy = ListNode()
        dummy.next = head
        curr = dummy

        while curr.next:
            ## dont knwo how to write it in the comments -_-
            if curr.next.next and curr.next.val == curr.next.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return dummy.next
