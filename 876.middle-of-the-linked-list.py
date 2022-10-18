# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ## one way is traversing the whole list and counting the nodes
        ## then traversing again up to the second mid

        ## but there is another interesting way. It asks to get the middle point.
        ## so we can iterate the list faster in 2x and 1x.

        normal_speed = head
        double_speed = head

        ## choosing this while condition is the trickiest part ig
        ## we need double_speed pointer here because this is making the longest jumps
        while double_speed and double_speed.next:
            ## its like, if someone is running 2x speed and reaches 2km. then someone running 1x speed will reach 1km or half
            ##in the same amount of time
            normal_speed = normal_speed.next
            double_speed = double_speed.next.next

        return normal_speed