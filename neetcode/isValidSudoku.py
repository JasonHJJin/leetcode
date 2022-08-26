from collections import defaultdict
from warnings import WarningMessage


def isValidSudoku(self, board) -> bool:
    rows = defaultdict(set)
    cols = defaultdict(set)
    mats = defaultdict(set)

    for i in range(9):
        for j in range(9):
            if board[i][j] == ".":
                continue

            if (board[i][j] in rows[i]) or (board[i][j] in cols[j]) or (board[i][j] in mats[(i//3, j//3)]):
                return False

            else:
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                mats[(i//3, j//3)].add(board[i][j])

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

print(isValidSudoku("", board))


