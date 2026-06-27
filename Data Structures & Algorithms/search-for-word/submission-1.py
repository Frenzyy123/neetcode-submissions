class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(visited,row_num,col_num,word):
            if not word:
                return True
            if col_num < 0 or col_num == len(board[0]) or row_num < 0 or row_num == len(board) or (row_num,col_num) in visited:
                return
            if word[0] != board[row_num][col_num]:
                return
            visited.add((row_num,col_num))
            if dfs(visited,row_num,col_num - 1,word[1:]) == True:
                return True
            if dfs(visited,row_num - 1,col_num,word[1:]) == True:
                return True
            if dfs(visited,row_num,col_num + 1,word[1:]) == True:
                return True
            if dfs(visited,row_num + 1,col_num,word[1:]) == True:
                return True
            visited.remove((row_num,col_num))
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if dfs(set(),i,j,word) == True:
                        return True
        return False


