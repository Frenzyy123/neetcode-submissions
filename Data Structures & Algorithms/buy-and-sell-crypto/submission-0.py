class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        curr_min = prices[0]
        for i in range(len(prices)):
            if prices[i] < curr_min:
                curr_min = prices[i]
            else:
                curr_profit = prices[i] - curr_min
                max_profit = max(curr_profit,max_profit)
        

        return max_profit