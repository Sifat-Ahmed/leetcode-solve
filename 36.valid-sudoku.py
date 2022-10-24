from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ## will just insert the values in the map and then check if its already there or not
        ## for rows
        rows = [set() for _ in range(9)]
        ## for columns
        columns = [set() for _ in range(9)]
        ## for 3x3 squares
        mini_square = [[set() for _ in range(3)] for i in range(3)]

        for i in range(9):
            for j in range(9):
                ## ignore if its a blank position
                if board[i][j] == ".":
                    continue
                ## now checking if the digit is already in the corresponding map
                elif board[i][j] in rows[i] or board[i][j] in columns[j] or board[i][j] in mini_square[i // 3][j // 3]:
                    return False

                ## add the board value to the corresponding maps
                rows[i].add(board[i][j])
                columns[j].add(board[i][j])
                mini_square[i // 3][j // 3].add(board[i][j])

        ## if code reaches up to this then it's a valid sudoku
        return True


if __name__ == '__main__':
    s = Solution()
    test_cases = [["8", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                  [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                  ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                  [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                  [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

    print(s.isValidSudoku(test_cases))
