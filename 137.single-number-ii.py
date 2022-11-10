from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ## hashmap, count the numbers
        hashmap = {}

        for num in nums:
            if num in hashmap.keys():
                hashmap[num] += 1
            else:
                hashmap[num] = 1

        for i, j in enumerate(hashmap):
            if hashmap[j] == 1:
                return j