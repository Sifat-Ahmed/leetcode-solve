from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ## bfs?

        ## first checking if the grid is empty or not
        if len(grid) == 0: return -1
        ## getting the number of rows and columns of the grid
        rows, cols = len(grid), len(grid[0])

        fresh_oranges = 0
        ## Queue // Will be using list with pop(0)
        rotten_oranges = list()

        for r in range(rows):
            for c in range(cols):
                ## checking the condition of the orange in the grid
                if grid[r][c] == 2:
                    rotten_oranges.append((r, c))
                ## counting the number of fresh oranges
                ## we need this in the future to calculate the remaining oranges
                elif grid[r][c] == 1:
                    fresh_oranges += 1

        minutes_passed = 0

        ## as long as we have rotten oranges and fresh oranges, we need to visit them
        while rotten_oranges and fresh_oranges > 0:
            ## so first updating the time because we are visiting level by level.
            minutes_passed += 1

            ## we only need the loop, not the loop var and loop through all the rotten oranges
            for _ in range(len(rotten_oranges)):
                r, c = rotten_oranges.pop(0)

                ## traversing the diagonal positions
                for x, y in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    ## getting the neighbour coordinates
                    nx, ny = r + x, c + y

                    ## now we need to check if the coordinates are valid
                    if nx < 0 or ny < 0 or nx >= rows or ny >= cols: continue

                    ## now checking if the current apple which we are visiting
                    ## it can be a blank space or a rotten, or a fresh
                    ## do nothing if rotten or blank

                    if grid[nx][ny] == 0 or grid[nx][ny] == 2: continue

                    ## now its certain that there is a fresh orange

                    fresh_oranges -= 1

                    ## update the grid position
                    grid[nx][ny] = 2

                    rotten_oranges.append((nx, ny))

        if fresh_oranges == 0: return minutes_passed
        return -1