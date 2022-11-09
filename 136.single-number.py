from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0

        ## could have done with hash
        ## learned something new with XOR

        for n in nums: result ^= n

        return result