from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ## Just after a glimpse, hashmap crossed my mind
        ## also I can try two pointer approach on sorted array

        ## I will make the hashmap with the one that has more numbers
        ## so there is a possibility that any of them is bigger
        ## if one is bigger than the other then I just swap them\
        ## I am making the hashmap with the biggest one here
        if len(nums1) < len(nums2):
            ## swap
            nums1, nums2 = nums2, nums1

        hashmap = dict()

        ## So for each number on the biggest list,
        ## if the number is in the map then increase, because intersection its not unique intersection
        ## if not just initialize with 1
        for number in nums1:
            if number in hashmap.keys():
                hashmap[number] += 1
            else:
                hashmap[number] = 1

        result = list()

        ## now for the 2nd list, if its in hashmap, then check the count and insert it in the results
        ## order doesn't matter so no need to sort
        for number in nums2:
            if number in hashmap.keys():
                if hashmap[number] > 0:
                    ## already found so decrease
                    hashmap[number] -= 1
                    result.append(number)

        return result


if __name__ == '__main__':
    s = Solution()

    nums1 = [[1,2,2,1], [4,9,5]]
    nums2 = [[2,2], [9,4,9,8,4]]

    for n1, n2 in zip(nums1, nums2):
        print('Test case {}: {} -> {}'.format(n1, n2,  s.intersect(n1, n2)))
