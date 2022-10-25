from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = list()

        for i in range(numRows):
            result.append([1])

            if i > 1:
                for j in range(i - 1):
                    result[i].append(result[i - 1][j] + result[i - 1][j + 1])

            if i > 0:
                result[i].append(1)

        return result