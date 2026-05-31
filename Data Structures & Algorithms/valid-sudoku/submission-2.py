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
                if board[i][j] in rows[i]:
                    return False
                if board[i][j] in cols[j]:
                    return False
                if board[i][j] in squares[3 * (i // 3) + j // 3]:
                    return False
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                squares[3 * (i // 3) + j // 3].add(board[i][j])
        return True