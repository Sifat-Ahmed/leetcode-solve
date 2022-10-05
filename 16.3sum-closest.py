"""
problem: https://leetcode.com/problems/3sum-closest/
Date: 03/10/2022

"""
class Solution(object):

    def threeSumClosest(self, nums, target):
        ## The problem says order doesn&t matter
        ## So sorting the array
        nums.sort()
        n = len(nums)
        answer = 0
        diff = 999999

        ## This is a triplet problem. So picking 3 positions with one pivot and left/right pointers
        for i in range(n):
            left, right = i + 1, n - 1
            ## This variable will be used to track the minimum distance

            while left < right:
                sums = nums[i] + nums[left] + nums[right]

                if sums == target:
                    return sums

                if abs(sums - target) < diff:
                    print('{} and {} - {} // {}'.format(sums, target, abs(sums - target), diff))
                    diff = abs(sums - target)
                    answer = sums

                if sums > target:
                    ## jump one step backward
                    ## because we need to decrease the sum
                    right -= 1
                elif sums < target:
                    left += 1
        return answer


if __name__ == '__main__':
    s = Solution()
    case = [[1, 1, 1, 0], [0, 0, 0]]

    for i in range(len(case)):
        print('Test case {}: {} -> {}'.format(i + 1, case[i], s.threeSumClosest(case[i], -100)))
