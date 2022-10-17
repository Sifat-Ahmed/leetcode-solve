class Solution:
    def searchInsert(self, nums, target: int) -> int:
        ## just do a binary search and return the lowest/left position
        ## in case its blank, then just insert it at 0th index
        if not nums: return 0

        left, right = 0, len(nums)-1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target: return mid

            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return left


if __name__ == '__main__':
    s = Solution()
    lists = [[1,3,5,6], [1,3,5,6], [1,3,5,6]]
    target = [5, 2, 7]

    for i in range(len(lists)):
        print('Test case {}: Insert {} to {} -> {}'.format(i+1,  target[i], lists[i], s.searchInsert(lists[i], target[i])))