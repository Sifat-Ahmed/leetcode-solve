# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        ## only execptional case is k == 1
        ## which returns the same linked list
        ## I didn't notice this until I got an TLE. This is Basic :'(
        if k == 1: return head

        values_to_reverse = list()
        # counter = 1
        new_head = temp = dummy = head

        ## wasn't sure how to do it. The only approach that clicked was reverse the sublist of k-length tree
        ## then add the remaining items to the list

        ## traverse until k-th element
        ## then create a new list with the reverse
        ## connect it to starting position
        ## repeat it until done

        ## if any item remains, create a new list and connect it

        while dummy:
            ## appending the values until k-th element
            values_to_reverse.append(dummy.val)
            ## k-th element found?
            if len(values_to_reverse) == k:
                ## until the list is empty
                while values_to_reverse:
                    ## create a new node
                    new = ListNode(values_to_reverse.pop())
                    ## move forward with a new link
                    temp.next = new
                    temp = temp.next
            ## move the main list forward
            dummy = dummy.next
        ## still some values left? it should be if len(linked list) % k != 0
        ## so just put them in the new link one by one, But be careful, don't reverse them
        while values_to_reverse:
            new = ListNode(values_to_reverse.pop(0))
            temp.next = new
            temp = temp.next

        ## return the new tree from head reference
        return new_head.next