class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        distances = [0] * (len(cost) + 1)
        distances[0] = 0
        distances[1] = 0
        for i in range(2,len(distances)):
            distances[i] = min((distances[i - 1] + cost[i - 1]),(distances[i - 2] + cost[i - 2]))
        return distances[-1]
