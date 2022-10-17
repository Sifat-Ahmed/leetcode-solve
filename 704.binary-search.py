class Solution:
    def search(self, nums: List[int], target: int) -> int:
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
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left if nums[left] == target else -1