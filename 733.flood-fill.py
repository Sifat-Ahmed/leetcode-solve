from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        initial_color = image[sr][sc]

        def dfs(x, y):
            if x < 0 and x > len(image): return
            if y < 0 and y > len(image[0]): return
            if image[x][y] != initial_color: return
            if image[x][y] == color: return

            image[x][y] = color

            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)

        dfs(sr, sc)

        return image
