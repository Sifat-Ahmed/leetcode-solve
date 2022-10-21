from typing import List


class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        ## first we need to check if it can be reshaped
        ## r * c == size(mat) or impossible to reshape

        m, n = len(mat), len(mat[0])

        ## if they can't be reshaped then just return the original array
        if m * n != r * c: return mat
        result = [[0 for i in range(c)] for j in range(r)]

        for i in range(r * c):
            result[i // c][i % c] = mat[i // n][i % n]

        return result

if __name__ == '__main__':
    s = Solution()

    nums1 = [[[1,2],[3,4]]]

    for i in range(len(nums1)):
        print('Test case {}: {} -> {}'.format(i+1, nums1[i],  s.matrixReshape(nums1[i], 2, 4)))
