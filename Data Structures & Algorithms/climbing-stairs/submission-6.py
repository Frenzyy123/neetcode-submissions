class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        positions = [1,2]
        for i in range(n - 2):
            tmp = positions[1]
            positions[1] = positions[0] + positions[1]
            positions[0] = tmp
        return positions[-1]