class Solution:
    def removeDuplicates(self, nums) -> int:
        j = 0
        for i in range(1, len(nums)):
            ## if not duplicate then just increase j
            if nums[j] != nums[i]:
                j += 1
                ## update j-th position with i-th value
                nums[j] = nums[i]
        ## just return j+1
        return j + 1

if __name__ == '__main__':
    s = Solution()
    case = [[0,0,0,0,1,2,3,3,3,5]]
    for i in range(len(case)):
        print('Test case {}: {} -> {}'.format(i + 1, case[i], s.removeDuplicates(case[i])))