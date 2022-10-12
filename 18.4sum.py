class Solution:
    def fourSum(self, nums, target: int):
        if len(nums) < 4: return []
        nums.sort()
        result = list()

        ## first picking two points
        ## inside the m there will be two pivots/pointers that will update for the two point pair
        for i in range(len(nums)):
            ## if the number in the current index and the previous index are same then just ignore it
            ## First checking if index variable is greate than 0 or not
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            ## same for j
            for j in range(i + 1, len(nums)):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                ## choosing two pointers
                left = j + 1
                right = len(nums) - 1
                temp = 0

                while left < right:
                    temp = nums[i] + nums[j] + nums[left] + nums[right]
                    ## its already sorted so if the sum is bigger than the target then we need to reduce the right pointer
                    ## because larger numbers are on the right side
                    if temp > target:
                        right -= 1
                    ## vice versa for left
                    elif temp < target:
                        left += 1
                    else:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        ## just ignore until same occurances are there
                        ## for both left and right
                        t_val = nums[left]
                        while left < right and t_val == nums[left]:
                            left += 1
                        t_val = nums[right]
                        while right > left and t_val == nums[right]:
                            right -= 1

        return result


if __name__ == '__main__':
    s = Solution()
    case = [[1,0,-1,0,-2,2], [2,2,2,2,2]]
    target = [0, 8]

    for i in range(len(case)):
        print('Test case {}: {} -> {}'.format(i + 1, case[i], s.fourSum(case[i], target[i])))
