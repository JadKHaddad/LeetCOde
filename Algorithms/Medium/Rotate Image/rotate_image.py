from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l = len(matrix) - 1

        def swap(i, j, x, y):
            temp = matrix[i][j]
            matrix[i][j] = matrix[x][y]
            matrix[x][y] = temp

        for i in range(0, int(l+1/2)):
            for j in range(i, l-i):
                swap(i, j, j, l-i)
                swap(i, j, l-i, l-j)
                swap(i, j, l-j, i)


matrix = [
    [5, 1, 9, 11],
    [2, 4, 8, 10],
    [13, 3, 6, 7],
    [15, 14, 12, 16]
]
Solution().rotate(matrix)
print(matrix)
