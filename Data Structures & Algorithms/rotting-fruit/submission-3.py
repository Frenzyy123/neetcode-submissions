from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minutes = 0
        que = deque()
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    que.append((i,j))
                    visited.add((i,j))
        while que:
            for i in range(len(que)):
                curr_rotten = que.popleft()
                neighbors = [[0,1],[0,-1],[-1,0],[1,0]]
                for i in neighbors:
                    if (curr_rotten[0] + i[0],curr_rotten[1] + i[1]) not in visited and curr_rotten[0] + i[0] > -1 and curr_rotten[0] + i[0] < len(grid) and curr_rotten[1] + i[1] < len(grid[0]) and curr_rotten[1] + i[1] > -1 and grid[curr_rotten[0] + i[0]][curr_rotten[1] + i[1]] == 1:
                        grid[curr_rotten[0] + i[0]][curr_rotten[1] + i[1]] = 2
                        que.append((curr_rotten[0] + i[0],curr_rotten[1] + i[1]))
                        visited.add((curr_rotten[0] + i[0],curr_rotten[1] + i[1]))
            if not que:
                break
            minutes += 1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        return minutes