class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        output = 0
        def dfs(r,c,visited):
            if r < 0 or c < 0 or r == len(grid) or c == len(grid[0]) or (r,c) in visited or grid[r][c] == '0':
                return
            visited.add((r,c))
            dfs(r,c - 1,visited)
            dfs(r,c + 1,visited)
            dfs(r - 1,c,visited)
            dfs(r + 1,c,visited)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '0' or (i,j) in visited:
                    continue
                else:
                    output += 1
                    dfs(i,j,visited)
        return output
