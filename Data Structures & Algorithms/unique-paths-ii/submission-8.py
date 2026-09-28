class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = -1

        def dfs(row,col):
            if row == len(obstacleGrid) or col == len(obstacleGrid[0]) or obstacleGrid[row][col] == -1:
                return 0
            if row == len(obstacleGrid) - 1 and col == len(obstacleGrid[0]) - 1:
                return 1
            
            if obstacleGrid[row][col] != 0 :
                return obstacleGrid[row][col]
            
            obstacleGrid[row][col] =  dfs(row + 1,col) + dfs(row, col + 1)
            return obstacleGrid[row][col]

        return dfs(0,0)
            