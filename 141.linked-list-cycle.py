from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None



class Solution:
    def hasCycle1(self, head: Optional[ListNode]) -> bool:
        if head is None or head.next is None:
            return False

        ## i will try this problem with two pointers, slow and fast
        ## fast will jump two positions and slow will jump one
        ## if there is a cycle fast and slow will point to same address at some point

        ## one jump
        slow = head.next
        ### two jump
        fast = head.next.next

        ## as long as we can make two jumps (We can always make one jump)
        while fast and fast.next:
            if slow == fast: return True

            slow = slow.next
            fast = fast.next.next

        return False

    ## method 2 just for interest
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        element = set()
        while head:
            if head not in element:
                element.add(head)
                head = head.next
            else:
                return True
        return False