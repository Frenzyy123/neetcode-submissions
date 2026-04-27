from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self,grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return - 1
        end_row = len(grid) - 1
        end_col = len(grid[0]) - 1
        visited = set()
        visited.add((0,0))
        length = 1
        queue = deque([(0,0)])
        while queue:
            for _ in range(len(queue)):
                r,c = queue.popleft() # r = queue[0][0] c = queue[0][1] queue.popleft()
                if r == end_row and c == end_col:
                    return length
                neighbors = [[1,0],[-1,0],[0,1],[0,-1],[1,1],[-1,-1]]
                for i,j in neighbors:
                    if (r + i,c + j) not in visited and r + i > -1 and r + i < len(grid) and c + j > - 1 and c + j < len(grid[0]) and grid[r + i][c + j] != 1:
                        queue.append((r + i,c + j))
                        visited.add((r + i,c + j)) 
            length += 1
        return -1
