class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        ## attempt 1: just concatenate the lists, sort them and get the median

        ## concatenating the lists
        nums = nums1 + nums2
        ## sorting the lists
        nums.sort()
        ## getting the number of elements in the list

        n = len(nums)

        ## if odd number of numbers then just return the middle element
        if n % 2 == 1: return nums[(n-1)//2]
        ## or just return the average of two middle elements
        else: return (nums[n//2 - 1] + nums[n//2]) / 2.0
        ## had to waste so much time because of not dividing by float ##ggs python versions


if __name__ == '__main__':
    s = Solution()
    # case1 = [[1, 2],]
    # case2 = [[3, 4],]
    # for i in range(len(case1)):
    #     print('Test case {}: {}, {} -> {}'.format(i + 1, case1[i], case2[i], s.findMedianSortedArrays(case1[i], case2[i])))

    print(s.findMedianSortedArrays([1,2], [3,4]))