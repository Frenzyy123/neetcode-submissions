class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        for i in range(1,amount + 1):
            for j in coins:
                if j > i:
                    continue
                else:
                    if dp[i - j] != float("inf") and 1 + dp[i - j] < dp[i] :
                        dp[i] = 1 + dp[i - j]
        if dp[amount] == float("inf"):
            return -1
        else:
            return dp[-1]