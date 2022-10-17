class Solution:
    def searchRange(self, nums, target: int):
        ## the description says to do it with complexity of O(log n)
        ## there are two ways that I can think of. One is first finding the target number with binary search
        ## then expanding to left and right from that position // possibly it would O(n) on worst case

        ## another is running two binary searches on left and right
        ## I will try the first one

        if not nums: return [-1, -1]

        left = 0
        right = len(nums)-1

        def search_left_right(nums, mid):
            left = right = mid

            ## searching if the number is same in the left
            while left > 0 and nums[left - 1] == target:
                left -= 1
            ## searching if the number is same on the right
            while right < len(nums) - 1 and nums[right + 1] == target:
                right += 1

            return [left, right]

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return search_left_right(nums, mid)
            else:
                if target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

        return [-1, -1]


if __name__ == '__main__':
    s = Solution()
    lists = [[5,7,7,8,8,10], [5,7,7,8,8,10], []]
    target = [8, 6, 0]

    for i in range(len(lists)):
        print('Test case {}: {} -> {}'.format(i+1, lists[i], s.searchRange(lists[i], target[i])))