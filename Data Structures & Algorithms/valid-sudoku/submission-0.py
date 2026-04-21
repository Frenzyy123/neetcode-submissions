from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        cols = {}
        squares = {}
        for i in range(9):
            rows[i] = set()
            cols[i] = set()
            squares[i] = set()
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                else:
                    square_number = 3 * (i // 3) + (j // 3)
                    if board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in squares[square_number]:
                        return False
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    squares[square_number].add(board[i][j])

        return True

