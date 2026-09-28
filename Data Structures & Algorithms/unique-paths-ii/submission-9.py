class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        col_counter = 0
        while col_counter < len(obstacleGrid[0]):
            if obstacleGrid[0][col_counter] == 1:
                while col_counter < len(obstacleGrid[0]):
                    obstacleGrid[0][col_counter] = 0
                    col_counter += 1
            else:
                obstacleGrid[0][col_counter] = 1
                col_counter += 1
        
        row_counter = 1
        while row_counter < len(obstacleGrid):
            if obstacleGrid[row_counter][0] == 1:
                while row_counter < len(obstacleGrid):
                    obstacleGrid[row_counter][0] = 0
                    row_counter += 1
            else:
                obstacleGrid[row_counter][0] = 1
                row_counter += 1
        for i in range(1,len(obstacleGrid)):
            for j in range(1,len(obstacleGrid[0])):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                else:
                    obstacleGrid[i][j] = obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1]
        return obstacleGrid[-1][-1]
        
