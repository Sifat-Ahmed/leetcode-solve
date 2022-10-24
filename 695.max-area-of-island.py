from typing import List


class Solution:

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ## I will try this with depth first search (DFS)

        m, n = len(grid), len(grid[0])
        max_value = 0

        def dfs(grid, i, j, m, n):
            ## cheking if the coordinates are outside the grid or its visited already
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == 0:
                return 0

            ## marking the grid position as visited
            grid[i][j] = 0

            return dfs(grid, i - 1, j, m, n) + dfs(grid, i + 1, j, m, n) + dfs(grid, i, j - 1, m, n) + dfs(grid, i, j + 1, m, n) + 1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    count = dfs(grid, i, j, m, n)
                    max_value = max(max_value, count)

        return max_value

if __name__ == '__main__':
    s = Solution()
    test_cases = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                  [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                  [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]

    print(s.maxAreaOfIsland(test_cases))
