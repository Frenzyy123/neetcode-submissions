class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        max_area = 0
        def dfs(r,c,visited):
            area = 1
            if r < 0 or c < 0 or r == len(grid) or c == len(grid[0]) or (r,c) in visited or grid[r][c] == 0:
                return 0 
            visited.add((r,c))
            area += dfs(r,c - 1,visited)
            area += dfs(r,c + 1,visited)
            area += dfs(r - 1,c,visited)
            area += dfs(r + 1,c,visited)
            return area

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0 or (i,j) in visited:
                    continue
                else:
                    surface = dfs(i,j,visited)
                    max_area = max(max_area,surface)
        return max_area
