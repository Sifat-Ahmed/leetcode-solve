from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        if not nums: return

        ## variables to hold the sum at ith step and result
        running_sum, result = 0, list()

        ## iterate over the list of numbers
        for num in nums:
            running_sum += num
            result.append(running_sum)

        return result