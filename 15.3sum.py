"""
problem: https://leetcode.com/problems/3sum
Date: 03/10/2022

"""

class Solution(object):

    def threeSum(self, nums):
        ## The problem says order doesn&t matter
        ## So sorting the array
        nums.sort()
        n = len(nums)
        answer = list()

        ## This is a triplet problem. So picking 3 positions with one pivot and left/right pointers
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]: continue
            left, right = i + 1, n - 1

            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    ## already sorted so jump one step forward
                    left += 1
                elif sum > 0:
                    ## jump one step backward
                    ## because we need to decrease the sum
                    right -= 1
                else:
                    ans = [nums[i], nums[left], nums[right]]
                    if ans not in answer:
                        answer.append(ans)
                        ## if match found go forward
                    left += 1
        return answer
if __name__ == '__main__':
    s = Solution()
    case = [[-1,0,1,2,-1,-4], [0,1,1], [0,0,0]]

    for i in range(len(case)):
        print('Test case {}: {} -> {}'.format(i + 1, case[i], s.threeSum(case[i])))