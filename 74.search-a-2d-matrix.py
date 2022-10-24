from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int):

        ## I am going to try a 2d Bin search. And attempting to run it through out the same loop.
        lo, hi = 0, len(matrix) - 1
        while lo <= hi:
            ## getting the middle row
            midRow = (lo + hi) // 2
            row = matrix[midRow]
            ## if the target is less than the first element of the selected row, then go one row back
            if target < row[0]:
                hi = midRow - 1
            ## if the target os greater than the last element then go one row forward
            elif target > row[-1]:
                lo = midRow + 1
            ## if target is inside the row[0] and row[-1]
            else:
                ## then doing a row wise binary search again
                l, r = 0, len(row) - 1
                while l <= r:
                    mid = (l + r) // 2
                    if row[mid] == target:
                        return True
                    elif target > row[mid]:
                        l = mid + 1
                    else:
                        r = mid - 1
                return False

if __name__ == '__main__':
    s = Solution()

    test_case = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 20

    print(s.searchMatrix(test_case, target))
