from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        ## My first attempt was to try a two pointer approach.
        ## This would have worked unless there was an edge case
        ## Still I will keep this as comment

        # left, right = 1, len(nums)-2
        # left_sum , right_sum = nums[0], nums[len(nums)-1]

        # while left <= right:

        #     print('sum', left_sum, right_sum)
        #     if left_sum < right_sum:
        #         left_sum += nums[left]
        #         left += 1
        #     elif left_sum > right_sum:
        #         right_sum += nums[right]
        #         right -= 1

        #     else:
        #         return left

        # return -1

        total = sum(nums)
        leftSum = 0

        for i in range(len(nums)):
            total -= nums[i]

            if total == leftSum: return i
            leftSum += nums[i]

        return -1