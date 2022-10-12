# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ## creating two same nodes
        ## one to hold the start position
        ## and one to iterate
        temp = head = ListNode()

        ## if both lists are available // or the comparison won&t work
        ## its like a chain method, where we cut a point, insert it and do the linking
        while list1 and list2:
            if list1.val < list2.val:
                ## if the value is smaller
                ## we need this list1 node, bcz its smaller
                ## so add it to temporary chain
                temp.next = list1
                ## move forward with list1
                ## and jump one chain forward for temp
                list1, temp = list1.next, list1
            else:
                ## same as above
                temp.next = list2
                list2, temp = list2.next, list2

        ## for the remaining elements of any of them
        if list1 or list2:
            temp.next = list1 if list1 else list2

        return head.next