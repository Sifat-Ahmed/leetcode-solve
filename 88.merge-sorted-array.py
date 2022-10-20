from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        ### When I read this, on the first glimps it reminds me of insertion sort
        ### Another is insert nums2 in nums1 in the places of zero and do a in place sorting

        ## Attempting with insertion sort
        ## first combine both in nums1
        j = 0
        ## all values of nums1 from m to m+n are 0 because this is the size of nums2
        for i in range(m, m + n):  # Complexity O(n)
            nums1[i] = nums2[j]  # O(1)
            j += 1  # O(1)

        ## now doing an insertion sort
        for i in range(0, len(nums1)):  # O(n)
            key = nums1[i]  # O(1)
            j = i - 1  # O(1)
            while j >= 0 and nums1[j] > key:  # O(n * n) // in worst case
                nums1[j + 1] = nums1[j]

                j -= 1

            nums1[j + 1] = key


