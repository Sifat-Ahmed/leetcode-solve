# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ## this is the node we start working from
        current_node = ListNode()
        ## because we will move forward, we need to save the first node or it will be lost
        head = current_node

        ## keeping a carry bit because result can be more than 10
        carry = 0
        ## if node exists, or there is carry we write it

        ## 878 + 122 = 1000 is a good example
        while l1 or l2 or carry:
            ## taking the carry into account
            sum = carry
            ## if the node exists then take the value, add it and move on to the next node
            if l1:
                sum += l1.val
                ## moving on to the next node
                l1 = l1.next
            ## same for l2
            if l2:
                sum += l2.val
                l2 = l2.next
            ## getting the carry bit, normal division will give decimal results.
            carry = sum // 10
            ## creating a new node with the value of reminder
            next_node = ListNode(val=(sum % 10))
            ## creating a link
            current_node.next = next_node
            ## moving to the next node
            current_node = next_node

        ## returning the head node
        return head.next
