class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        islands = 0
        def dfs(row,col):
            if row < 0 or row == len(grid) or col < 0 or col == len(grid[0]):
                return
            if (row,col) in visited:
                return
            if grid[row][col] == '0':
                return
            visited.add((row,col))
            dfs(row,col + 1)
            dfs(row + 1,col)
            dfs(row - 1,col)
            dfs(row,col - 1)
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '0' or (i,j) in visited:
                    continue
                else:
                    islands += 1
                    dfs(i,j)

        return islands
