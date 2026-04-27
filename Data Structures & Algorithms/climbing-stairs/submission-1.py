class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        positions = [1,2]
        for i in range(n - 2):
            positions.append(positions[-1] + positions[-2])
        return positions[-1]