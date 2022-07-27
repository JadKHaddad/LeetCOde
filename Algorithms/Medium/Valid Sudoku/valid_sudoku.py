from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        column_dict = {}
        cells = [
            [{}, {}, {}],
            [{}, {}, {}],
            [{}, {}, {}],
        ]
        for i in range(0, 9):
            for j in range(0, 9):
                if board[i][j] == ".":
                    continue
                # check cell
                if board[i][j] in cells[int(i/3)][int(j/3)]:
                    return False
                cells[int(i/3)][int(j/3)][board[i][j]] = None
                # create a column dict
                if j not in column_dict:
                    column_dict[j] = {}
                # checking column
                if board[i][j] in column_dict[j]:
                    return False
                column_dict[j][board[i][j]] = None
                # checking row
                for k in range(j + 1, 9):
                    if board[i][j] == board[i][k]:
                        return False
        return True


board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]


print(Solution().isValidSudoku(board))
