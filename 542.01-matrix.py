from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        ## first we need a queue to save the child notes and visited set to track the nodes
        ## this is a multi-root problem, so we need to make sure to track it
        queue, visited = list(), set()

        ## getting the number of rows and cols
        rows, cols = len(mat), len(mat[0])

        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    queue.append([i, j])
                    visited.add((i, j))

        while queue:
            ## this is a list, so I need to pop the left most/ first position
            x, y = queue.pop(0)

            ## visiting the neighbours
            for (i, j) in ((x - 1, y), (x + 1, y), (x, y + 1), (x, y - 1)):
                ## checking the index range
                if i >= 0 and i < rows and j >= 0 and j < cols:
                    if (i, j) not in visited:
                        mat[i][j] = mat[x][y] + 1
                        visited.add((i, j))
                        queue.append([i, j])

        return mat