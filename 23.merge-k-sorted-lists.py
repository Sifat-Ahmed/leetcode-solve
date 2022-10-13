# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        ## Not sure about any other approach rather than traversing
        ## all the linked lists and getting the value in a list
        ## then sorting them and creating a new linked list with the
        ## sorted values

        ## total number of elements
        n = len(lists)
        ## save the values of the all the linked list here
        values_to_sort = list()

        ## traverse all the linked list
        for i in range(n):
            temp_head = lists[i]

            while temp_head:
                ## save the value and move on
                values_to_sort.append(temp_head.val)
                temp_head = temp_head.next

        ## sort the values // using Timesort // O(n.logn)
        values_to_sort.sort()

        ## creating a head reference and a temporary node
        new_head = temp_node = ListNode(-1)

        ## for each value create a new node and move on
        for val in values_to_sort:
            temp_node.next = ListNode(val)
            temp_node = temp_node.next

        ## return the head node reference
        return new_head.next