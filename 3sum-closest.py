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
        answer = None

        ## This is a triplet problem. So picking 3 positions with one pivot and left/right pointers
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]: continue
            left, right = i + 1, n - 1
            ## This variable will be used to track the minimum distance
            closest_distance = 99999

            while left < right:
                sum = nums[i] + nums[left] + nums[right]

                if sum == target:
                    return sum

                if abs(sum - target) < closest_distance:
                    closest_distance = abs(sum - target)
                    answer = sum

                elif abs(sum - target) > closest_distance:
                    ## jump one step backward
                    ## because we need to decrease the sum
                    right -= 1
                else:
                    left += 1
        return answer


if __name__ == '__main__':
    s = Solution()
    case = [[-1, 2, 1, -4], [0, 0, 0]]

    for i in range(len(case)):
        print('Test case {}: {} -> {}'.format(i + 1, case[i], s.threeSumClosest(case[i], 1)))
