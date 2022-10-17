## This is the easiest possible solution tbh

# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         if target in nums:
#             return nums.index(target)
#         else:
#             return -1

## lets try binary search, normal binary sort would have been so easy
## Just changing the mid to left or right but it's sorted and rotated on a pivot. Its more like sliced and side swapped

class Solution:
    ## for binary search the tricky part is switching the left and right wrt mid
    def search(self, nums, target):

        ## first pick left and right
        left, right = 0, len(nums) - 1

        ## iterate the array until left is less than right
        ## in normal binary search we divide the array into a mid position
        ## and check which side the target belongs wrt mid
        ## but this one is slightly tricky because it can be rotated at any index
        while left < right:
            ## calculating the mid position
            mid = (left + right) // 2

            ## if the value is in the mid, then just return the mid index
            if nums[mid] == target:
                return mid

            ## if the value at mid is bigger than left that means its still sorted
            if nums[mid] >= nums[left]:
                ## now we need to check if the target falls in the range of left and mid index
                if nums[left] <= target <= nums[mid]:
                    right = mid
                else:
                    left = mid + 1
            else:
                ## didn't pay much attention and ended up writing this if statement wrong
                if nums[mid] <= target <= nums[right]:
                    ##if nums[mid] >= target >= nums[right]:
                    left = mid
                else:
                    right = mid - 1

        return left if nums[left] == target else -1
