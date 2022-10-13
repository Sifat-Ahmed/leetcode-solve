# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ## for this problem, I will take three nodes
        ## current node -> first node -> second node // 1, 2, 3

        if not head or not head.next: return head

        ## will use this node to bring the second node to root
        dummy_node = ListNode(0, head)
        current = dummy_node

        while current.next and current.next.next:
            first, second = current.next, current.next.next
            ## bring the adjacent node to first position
            current.next = second
            ## first will get the next address of second
            first.next = second.next
            ## second is now behind first
            second.next = first

            ## jump two steps
            current = current.next.next

        return dummy_node.next