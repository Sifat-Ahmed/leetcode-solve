# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from typing import Optional


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        ## use two pointers, one jumps slow, and one fast 2x
        ## if there is a cycle, two nodes will be equivalent at some point
        slow, fast = head, head

        while fast and fast.next:
            ## slow jumping 1x
            slow = slow.next
            ## fast jumping 2x
            fast = fast.next.next

            ## if there is a cycle, at some point they will be same
            if slow == fast:
                ## now check again
                slow = head

                while slow != fast:
                    slow = slow.next
                    fast = fast.next

                return slow

