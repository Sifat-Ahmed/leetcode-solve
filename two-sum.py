class Solution(object):
    def twoSum(self, nums, target):
        required = {}
        for i in range(len(nums)):
            if target - nums[i] in required:
                return [required[target - nums[i]], i]
            else:
                required[nums[i]] = i

if __name__ == '__main__':
    s = Solution()
    case = [[2, 7, 11, 15], [3, 2, 4], [3, 3]]
    target = [9, 6, 6]

    for i in range(len(case)):
        print('Test case {}: {} -> {}'.format(i+1, case[i], s.twoSum(case[i], target[i])))