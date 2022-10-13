class Solution:
    def removeElement(self, nums,  val: int) -> int:
        j = 0
        for i in range(0, len(nums)):
            ## if not duplicate then just increase j
            if nums[i] != val:
                ## update j-th position with i-th value
                nums[j] = nums[i]
                j += 1
        ## just return j+1
        return j


if __name__ == '__main__':
    s = Solution()
    case = [[0,0,0,0,1,2,3,5], [1,1,1,1]]
    for i in range(len(case)):
        print('Test case {}: {} -> {}'.format(i + 1, case[i], s.removeElement(case[i], 0)))