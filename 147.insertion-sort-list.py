# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        currentNode = head
        previousNode = None
        while currentNode:
            if previousNode and previousNode.val > currentNode.val:
                # Detach the current node.
                detachedNode = currentNode
                previousNode.next = currentNode.next
                currentNode = currentNode.next
                # Attach the detached node at its correct position.
                # Check whether the detatched node needs to be attached at first position. If yes then update the head also.
                if head.val > detachedNode.val:
                    detachedNode.next = head
                    head = detachedNode
                else:
                    # Traverse the list from start and attach the detached node at its correct position.
                    tempPreviousNode = head
                    tempCurrentNode = head.next
                    while tempCurrentNode and tempCurrentNode.val <= detachedNode.val:
                        tempPreviousNode = tempCurrentNode
                        tempCurrentNode = tempCurrentNode.next
                    tempPreviousNode.next = detachedNode
                    detachedNode.next = tempCurrentNode
            else:
                previousNode = currentNode
                currentNode = currentNode.next
        return head