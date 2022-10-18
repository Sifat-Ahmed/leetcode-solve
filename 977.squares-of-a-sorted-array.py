class Solution:
    def sortedSquares(self, nums):
        left, right = 0, len(nums) - 1
        result = [0] * len(nums)
        writing_from_write = right

        while writing_from_write >= 0:
            l2 = nums[left] ** 2
            r2 = nums[right] ** 2

            if l2 > r2:
                result[writing_from_write] = l2
                # writing_from_write -= 1
                left = left + 1
            else:
                result[writing_from_write] = r2
                # writing_from_write -=1
                right = right - 1

            writing_from_write -= 1
        return result


if __name__ == '__main__':
    s = Solution()
    lists = [[-4, -1, 0, 3, 10], [-7, -3, 2, 3, 11], []]

    for i in range(len(lists)):
        print('Test case {}: {} -> {}'.format(i + 1, lists[i], s.sortedSquares(lists[i])))
