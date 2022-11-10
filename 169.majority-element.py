from autopep8 import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ## will try this with hash

        if len(nums) == 1: return nums[0]

        ## first decalring a hash/ dictionary
        hashmap = dict()

        for num in nums:
            ## check if the number id already a key
            if num in hashmap.keys():
                ## incraese the value once
                hashmap[num] += 1
                ## if its more than half of the size, then just return the number
                if hashmap[num] > len(nums) // 2:
                    return num
            ## intialize the map with the key and initial value of 1
            else:
                hashmap[num] = 1