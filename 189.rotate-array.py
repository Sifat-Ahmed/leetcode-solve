class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            num = nums.pop()
            nums.insert(0, num)


## in-place OP. So, no main, just tested on the site directly