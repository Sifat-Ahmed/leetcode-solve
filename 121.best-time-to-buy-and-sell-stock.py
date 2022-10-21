import math
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ## so this problem seems like a simple O(n) math problem
        ## the idea that hits me is find tomorrows price - todays price if tomorrows price > todays price
        ## then check if this is the maximum profit we can make

        left, right = 0, 1
        max_profit = 0
        while right < len(prices):
            if prices[left] < prices[right]:
                current_profit = prices[right] - prices[left]
                max_profit = max(max_profit, current_profit)
            else:
                left = right

            right += 1

        return max_profit

if __name__ == '__main__':
    s = Solution()

    nums1 = [[7,1,5,3,6,4], [7,6,4,3,1]]

    for i in range(len(nums1)):
        print('Test case {}: {} -> {}'.format(i+1, nums1[i],  s.maxProfit(nums1[i])))
