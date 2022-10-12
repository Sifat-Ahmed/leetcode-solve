class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head, n: int) :
        size, temp_ptr = 0, head

        while temp_ptr:
            temp_ptr = head.next
            size += 1

        ## if asking for the last element (from right)
        if n == size:
            return head.next

        size = size - (n+1)
        temp_ptr = head

        while size > 0:
            temp_ptr = temp_ptr.next
            size -= 1

        ## a -> b -> c
        ## to
        ## a -> c // a.next == b and a.next.next == b.next which is c
        temp_ptr.next = temp_ptr.next.next

        return head


