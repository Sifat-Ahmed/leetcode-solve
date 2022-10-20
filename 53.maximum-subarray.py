import math
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ## I had to take help for this problem until I found out about Kadane's Algo
        ## Bruteforce causes TLE

        maximum_now, maximum_upto_ith = 0, -math.inf

        for num in nums:
            maximum_now = max(num, maximum_now + num)
            ## This is the piece of the puzzle
            maximum_upto_ith = max(maximum_now, maximum_upto_ith)

        return maximum_upto_ith


if __name__ == '__main__':
    s = Solution()
    case = [[-2, 1, -3, 4, -1, 2, 1, -5, 4], [5, 4, -1, 7, 8]]
    target = [0, 8]

    for i in range(len(case)):
        print('Test case {}: {} -> {}'.format(i + 1, case[i], s.maxSubArray(case[i])))
