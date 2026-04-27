from collections import deque
class Solution:
    def orangesRotting(self,grid: List[List[int]]) -> int:
        minutes = 0
        visited = set()
        neighbors = [[1,0],[0,1],[-1,0],[0,-1]]
        start = None
        number_of_fresh = 0
        queue = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    visited.add((i,j))
                elif grid[i][j] == 1:
                    number_of_fresh += 1
                else:
                    queue.append((i,j))
        while queue:
            if number_of_fresh == 0:
                return minutes
            for i in range(len(queue)):
                r,c = queue.popleft()
                for i,j in neighbors:
                    if (r + i,c + j) in visited or r + i < 0 or r + i == len(grid) or c + j < 0 or c + j == len(grid[0]) or grid[r + i][c + j] == 2 :
                        continue
                    if grid[r + i][c + j] == 1:
                        number_of_fresh -= 1
                    queue.append((r + i,c + j))
                    visited.add((r + i,c + j))
            minutes += 1
        if number_of_fresh > 0:
            return -1
        else:
            return 0