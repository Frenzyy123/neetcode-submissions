class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        expo = 0
        for i in range(1, n + 1):
            if 2 ** expo == i:
                dp[i] = 1
                expo += 1
            else:
                dp[i] = 1 + dp[i - 2 ** (expo - 1)]
        return dp