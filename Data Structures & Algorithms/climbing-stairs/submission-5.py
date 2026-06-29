class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        
        steps = [0] * (n)
        steps[0] = 1 
        steps[1] = 2
        for i in range(2,len(steps)):
            steps[i] = steps[i - 1] + steps[i - 2]
        return steps[-1]
        