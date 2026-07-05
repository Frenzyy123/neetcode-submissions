class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount in coins:
            return 1
        if amount == 0:
            return 0
        if amount < min(coins):
            return - 1
        all_values = [float("inf")] * (amount + 1)
        for coin in coins:
            if coin < amount:
                all_values[coin] = 1
        for i in range(1,len(all_values)):
            if all_values[i] == 1:
                continue
            for j in range(len(coins) - 1,-1,-1):
                if coins[j] < i and all_values[i - coins[j]] != float("inf") and 1 + all_values[i - coins[j]] < all_values[i]:
                    all_values[i] =  1 + all_values[i - coins[j]]
        if all_values[-1] == float("inf"):
            return -1
        return all_values[-1]