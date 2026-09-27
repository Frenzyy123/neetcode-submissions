class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[0 for _ in range(n)] for _ in range(m)]
        def dfs(r,c,memo):
            if r == m or c == n:
                return 0
            if r == m - 1 and c == n - 1:
                return 1
            
            if memo[r][c] > 0:
                return memo[r][c]

            memo[r][c] = dfs(r + 1,c,memo) + dfs(r,c + 1,memo)
            return memo[r][c]
        
        return dfs(0,0,memo)