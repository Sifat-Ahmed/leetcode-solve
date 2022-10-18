class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        ## just swap from one side to another in-place using two pointers
        ## hello -> olleh from 2nd position to the left 'e' goes to the 2nd position from the right
        left, right = 0, len(s) - 1

        while left < right:
            ## pick one from the right position
            temp = s[right]
            ## exchange it with the left position
            s[right] = s[left]
            s[left] = temp

            ## increase left// move forward
            left += 1
            ## decrease right // move backward
            right -= 1



