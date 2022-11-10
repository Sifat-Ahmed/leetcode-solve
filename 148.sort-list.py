# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # making a list with linked list values
        values = []
        temp = head

        while temp:
            values.append(temp.val)
            temp = temp.next

        values.sort()
        if not values:
            return head

        # making a new linked list with sorted values
        temp = ListNode(values[0])

        newHead = temp

        for i in range(1, len(values)):
            newnode = ListNode(values[i])
            temp.next = newnode
            temp = temp.next

        return newHead